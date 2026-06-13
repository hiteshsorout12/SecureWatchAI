import cv2

from camera.camera_manager import (
    camera_manager
)


streaming = False


def start_camera():

    global streaming

    if streaming:
        return

    camera_manager.start()

    streaming = True

    print("📹 Live Camera Started")


def stop_camera():

    global streaming

    streaming = False

    camera_manager.stop()

    print("📹 Live Camera Stopped")


import time

def generate_frames():

    global streaming

    while streaming:

        frame = camera_manager.get_frame()

        if frame is None:
            time.sleep(0.01)
            continue

        success, buffer = cv2.imencode(
            ".jpg",
            frame
        )

        if not success:
            continue

        yield (

            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"

        )

    camera_manager.stop()