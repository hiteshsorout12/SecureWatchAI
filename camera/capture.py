import cv2
import time
import socket

from datetime import datetime

from face_recognition_module.recognizer import recognize_face
from camera.camera_service import open_camera
from camera.evidence_recorder import evidence_recorder

from models import event
from services.event_service import create_event
from services.evidence_folder import create_evidence_folder
from services.evidence_service import create_evidence
from services.audit_service import create_audit_log
from services.risk_engine import calculate_risk
from services.socket_service import (
    send_live_alert,
    publish_event,
    publish_evidence,
    publish_risk,
    publish_analytics,
    publish_timeline
)
from services.security_session import security_session
from services.security_session_service import start_session
from services.evidence_metadata import save_metadata
from services.evidence_folder import create_evidence_folder

from notifications.email_service import (
    send_email_alert,
    send_email_async
)


def capture_photo():
    print("🔥 NEW CAPTURE VERSION")

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

        event = create_evidence_folder()
        event_id = event["event_id"]
        event_folder =event["folder"]
        display_time = datetime.now().strftime(
            "%A, %d %B %Y | %I:%M:%S %p"
        )
        photo_path = str(
            event_folder / "photo.jpg"
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
            
            if camera is not None:
                camera.release()
                camera = None
            cv2.destroyAllWindows()

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
        
        security_session.start()

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
        
        start_session(
            session_type="EMERGENCY",
            risk_score=risk["risk_score"],
            status=risk["risk_level"]
        )
        
        print(
            f"Risk Score: {risk['risk_score']}"
        )

        print(
            f"Risk Level: {risk['risk_level']}"
        )
        
        send_email_async(
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

        send_live_alert(
            title="📧 Email Started",
            message="Emergency email is being sent in background.",
            level="info"
        )
        
        create_event(
            event_id=event_id,
            event_type="CAMERA_CAPTURE",
            risk_score=risk["risk_score"],
            status=risk["risk_level"]
        )

        def video_finished(video_path):
            print("🎥 Video Ready:", video_path)
            from pathlib import Path
            folder = Path(video_path).parent
            save_metadata(
                folder=folder,
                risk=risk,
                owner=False,
                event_type="CAMERA_CAPTURE",
                photo=photo_path,
                video=video_path,
                audio=str(folder / "audio.wav")
            )
            
            create_evidence(
                event_id=event_id,
                photo_path=photo_path,
                video_path=video_path,
                audio_path=str(folder / "audio.wav")
            )

            send_live_alert(
                title="🎥 Video Saved",
                message="Evidence recording completed.",
                level="success"
            )

        evidence_recorder.record_async(
            event_folder=event_folder,
            callback=video_finished,
            post_seconds=10
        )

        try:

            publish_event({
                "event_id": event_id,
                "event_type": "CAMERA_CAPTURE",
                "risk_level": risk["risk_level"]
            })

            publish_evidence({
                "event_id": event_id,
                "photo_path": photo_path,
                "video_path": "PROCESSING"
            })

            publish_risk({
                "risk_score": risk["risk_score"],
                "risk_level": risk["risk_level"]
            })

            publish_analytics()

            publish_timeline()

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

            send_live_alert(
                title="✅ Photo Saved",
                message="Photo saved. Video is processing in background.",
                level="success"
            )

        except Exception as e:

            print("Database Error:", e)

    finally:

        if camera is not None:
            camera.release()

        cv2.destroyAllWindows()

        security_session.stop()


if __name__ == "__main__":

    capture_photo()