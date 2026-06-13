from collections import deque
import threading
import time

import cv2

from camera.camera_manager import camera_manager


class VideoBuffer:

    def __init__(

        self,

        seconds=5,

        fps=20

    ):

        self.fps = fps

        self.max_frames = seconds * fps

        self.buffer = deque(
            maxlen=self.max_frames
        )

        self.running = False

        self.thread = None

        self.lock = threading.Lock()

    # ----------------------------
    # Start Buffer
    # ----------------------------

    def start(self):

        if self.running:
            return

        camera_manager.start()

        self.running = True

        self.thread = threading.Thread(

            target=self._update,

            daemon=True

        )

        self.thread.start()

        print(
            "🎥 Video Buffer Started"
        )

    # ----------------------------
    # Update Buffer
    # ----------------------------

    def _update(self):

        delay = 1 / self.fps

        while self.running:

            frame = camera_manager.get_frame()

            if frame is not None:

                with self.lock:

                    self.buffer.append(
                        frame.copy()
                    )

            time.sleep(delay)

    # ----------------------------
    # Get Frames
    # ----------------------------

    def get_frames(self):

        with self.lock:

            return list(self.buffer)

    # ----------------------------
    # Stop Buffer
    # ----------------------------

    def stop(self):

        self.running = False

        if self.thread:

            self.thread.join(
                timeout=1
            )

        camera_manager.stop()

        print(
            "🎥 Video Buffer Stopped"
        )


video_buffer = VideoBuffer()