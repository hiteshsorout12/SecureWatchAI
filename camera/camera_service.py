import cv2


def open_camera():

    camera = cv2.VideoCapture(
        0,
        cv2.CAP_DSHOW
    )

    if not camera.isOpened():

        print(
            "Camera Not Found"
        )

        return None

    return camera