from camera.capture import (
    capture_photo
)


def remote_capture():

    print(
        "Remote Capture Triggered"
    )

    capture_photo()

    return {
        "message":
        "Capture Triggered"
    }