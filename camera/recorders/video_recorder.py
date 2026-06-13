import cv2
import threading
import time

from camera.camera_manager import camera_manager


class VideoRecorder:

    def __init__(self):

        self.writer = None
        self.recording = False
        self.thread = None

        self.fps = 20
        height, width = frame.shape[:2]
        self.frame_size = (width, height)

    # -------------------------
    # Start Recording
    # -------------------------

    def start(self, filename):

        if self.recording:
            return

        self.writer = cv2.VideoWriter(
            filename,
            cv2.VideoWriter_fourcc(*"mp4v"),
            self.fps,
            self.frame_size
        )

        self.recording = True

        self.thread = threading.Thread(
            target=self._record,
            daemon=True
        )

        self.thread.start()

        print("🎥 Video Recording Started")

    # -------------------------
    # Recording Loop
    # -------------------------

    def _record(self):

        delay = 1 / self.fps

        while self.recording:

            frame = camera_manager.get_frame()

            if frame is not None:

                self.writer.write(frame)

            time.sleep(delay)

    # -------------------------
    # Stop
    # -------------------------

    def stop(self):

        if not self.recording:
            return

        self.recording = False

        if self.thread:

            self.thread.join()

        if self.writer:

            self.writer.release()

            self.writer = None

        print("🎥 Video Recording Stopped")


video_recorder = VideoRecorder()