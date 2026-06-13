import threading

from camera.capture import (
    capture_photo
)


def remote_capture():

    print(
        "Remote Capture Triggered"
    )

    threading.Thread(
        target=capture_photo,
        daemon=True
    ).start()

    return {
        "success": True,
        "message": "Capture Started"
    }