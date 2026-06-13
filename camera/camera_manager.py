import cv2
import threading
import time


class CameraManager:

    def __init__(self):

        self.camera = None
        self.frame = None

        self.lock = threading.Lock()

        self.running = False

        self.thread = None

        self.clients = 0

    # ----------------------------
    # Start Camera
    # ----------------------------

    def start(self):

        with self.lock:

            self.clients += 1

            if self.running:
                return

            print("📷 Opening Camera...")

            self.camera = cv2.VideoCapture(
                0,
                cv2.CAP_DSHOW
            )

            if not self.camera.isOpened():

                self.camera = None
                self.clients = 0

                raise Exception(
                    "Unable to open webcam."
                )

            self.camera.set(
                cv2.CAP_PROP_FRAME_WIDTH,
                1280
            )

            self.camera.set(
                cv2.CAP_PROP_FRAME_HEIGHT,
                720
            )

            self.camera.set(
                cv2.CAP_PROP_FPS,
                30
            )

            self.camera.set(
                cv2.CAP_PROP_BUFFERSIZE,
                1
            )

            self.running = True

            self.thread = threading.Thread(
                target=self._reader,
                daemon=True
            )

            self.thread.start()

        # Give webcam time to warm up
        time.sleep(0.5)

        # Wait until first frame arrives
        for _ in range(30):

            if self.frame is not None:

                print("✅ Camera Ready")

                return

            time.sleep(0.1)

        print("⚠ Camera Started (No Frame Yet)")

    # ----------------------------
    # Background Reader
    # ----------------------------

    def _reader(self):

        print("📷 Reader Thread Started")

        while self.running:

            success, frame = self.camera.read()

            if success:

                with self.lock:

                    self.frame = frame.copy()

            else:

                time.sleep(0.05)

    # ----------------------------
    # Latest Frame
    # ----------------------------

    def get_frame(self):

        with self.lock:

            if self.frame is None:

                return None

            return self.frame.copy()

    # ----------------------------
    # Stop Camera
    # ----------------------------

    def stop(self):

        with self.lock:

            if self.clients > 0:

                self.clients -= 1

            if self.clients > 0:

                return

            self.running = False

        if self.thread is not None:

            self.thread.join(timeout=1)

            self.thread = None

        if self.camera is not None:

            self.camera.release()

            self.camera = None

        self.frame = None

        print("🛑 Camera Released")

    # ----------------------------
    # Status
    # ----------------------------

    def is_running(self):

        return self.running


camera_manager = CameraManager()