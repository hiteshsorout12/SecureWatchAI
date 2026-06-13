from camera.camera_manager import camera_manager


class SharedCamera:

    def __init__(self):

        camera_manager.start()

    def read(self):
        import time
        for _ in range(30):      # wait up to ~3 seconds
            frame = camera_manager.get_frame()
            if frame is not None:
                return True, frame
            time.sleep(0.1)
        return False, None

    def release(self):

        camera_manager.stop()

    def isOpened(self):

        return camera_manager.is_running()


def open_camera():

    try:

        return SharedCamera()

    except Exception as e:

        print(
            "Camera Error:",
            e
        )

        return None