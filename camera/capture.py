import cv2
import time
import socket

from datetime import datetime

from face_recognition_module.recognizer import recognize_face
from camera.camera_service import open_camera
from camera.video_capture import record_video

from services.event_service import create_event
from services.evidence_service import create_evidence
from services.audit_service import create_audit_log
from services.risk_engine import calculate_risk
from services.socket_service import send_live_alert

from notifications.email_service import send_email_alert


def capture_photo():

    camera = None

    try:

        for _ in range(3):

            camera = open_camera()

            if camera is not None:
                break

            time.sleep(0.5)

        if camera is None:

            print(
                "Camera Not Available"
            )

            return

        time.sleep(0.2)

        ret = False
        frame = None

        for _ in range(3):

            ret, frame = camera.read()

            if ret:
                break

            time.sleep(0.2)

        if not ret:

            print(
                "Photo Capture Failed"
            )

            return

        file_timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        display_time = datetime.now().strftime(
            "%A, %d %B %Y | %I:%M:%S %p"
        )

        photo_path = (
            f"evidence/photos/{file_timestamp}.jpg"
        )

        saved = cv2.imwrite(
            photo_path,
            frame
        )

        if not saved:

            print(
                "Photo Save Failed"
            )

            return

        print(
            "Photo Saved:",
            photo_path
        )

        # CREATE DASHBOARD URL BEFORE FACE CHECK

        try:

            local_ip = socket.gethostbyname(
                socket.gethostname()
            )

        except:

            local_ip = "127.0.0.1"

        dashboard_url = (
            f"http://{local_ip}:5000"
        )

        is_owner = recognize_face(
            photo_path
        )

        if is_owner:

            print(
                "OWNER DETECTED"
            )

            send_email_alert(
                subject="✅ SecureWatch Login Notification",
                body=f"""
Laptop accessed successfully.

Time:
{display_time}

Face Recognition:
OWNER VERIFIED

Dashboard:
{dashboard_url}

Status:
SAFE LOGIN
"""
            )

            return

        print(
            "INTRUDER DETECTED"
        )
        
        send_live_alert(
            title="🚨 Intruder Detected",
            message="Unknown face detected. Capturing evidence...",
            level="danger"
        )

        risk = calculate_risk(
            failed_login=True,
            unknown_face=True,
            multiple_attempts=False
        )

        print(
            f"Risk Score: {risk['risk_score']}"
        )

        print(
            f"Risk Level: {risk['risk_level']}"
        )

        try:

            send_email_alert(
                subject="🚨 SecureWatch Intruder Alert",
                body=f"""
🚨 HIGH RISK INTRUDER DETECTED

📅 Time:
{display_time}

🎯 Risk Score:
{risk['risk_score']}

⚠️ Risk Level:
{risk['risk_level']}

🛡️ Dashboard:
{dashboard_url}

📍 Live Tracking:
{dashboard_url}/location

📂 Evidence Center:
{dashboard_url}/evidence

📜 Intrusion History:
{dashboard_url}/history

📸 Evidence:
Open dashboard to view photos and videos.

SecureWatch AI Security System
""",
                attachment_path=photo_path
            )

            print(
                "Alert Email Sent"
            )
            
            send_live_alert(
                title="📧 Email Sent",
                message="Emergency email successfully delivered.",
                level="success"
            )

        except Exception as e:

            print(
                "Email Failed:",
                e
            )

        video_path = record_video(5)

        try:

            event_id = create_event(
                event_type="CAMERA_CAPTURE",
                risk_score=risk["risk_score"],
                status=risk["risk_level"]
            )

            create_evidence(
                event_id=event_id,
                photo_path=photo_path,
                video_path=video_path,
                audio_path=""
            )

            create_audit_log(
                action="PHOTO_CAPTURED",
                module="CAMERA",
                details=f"Photo saved at {photo_path}",
                status="SUCCESS"
            )

            create_audit_log(
                action="RISK_ANALYZED",
                module="RISK_ENGINE",
                details=(
                    f"Risk Score={risk['risk_score']}, "
                    f"Risk Level={risk['risk_level']}"
                ),
                status="SUCCESS"
            )

            print(
                "Workflow Completed"
            )
            
            send_live_alert(
                title="✅ Evidence Saved",
                message="Photo, video and logs saved successfully.",
                level="success"
            )

        except Exception as e:

            print(
                "Database Error:",
                e
            )

    finally:

        if camera is not None:
            camera.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":

    capture_photo()