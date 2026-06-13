import cv2
import os
import subprocess
import threading
import time

import soundfile as sf

from camera.video_buffer import video_buffer
from camera.audio_buffer import audio_buffer
from camera.camera_manager import camera_manager

FFMPEG_PATH = r"C:\Users\hitesh\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"


class EvidenceRecorder:

    def __init__(self):

        self.fps = 20
        self.frame_size = (1280, 720)

    def record(
        self,
        event_folder,
        post_seconds=10
    ):

        print("🚨 Recording Evidence...")
        
        camera_manager.start()
        temp_video = str(event_folder / "video_temp.mp4")
        temp_audio = str(event_folder / "audio.wav")
        final_video = str(event_folder / "video.mp4")

        writer = cv2.VideoWriter(
            temp_video,
            cv2.VideoWriter_fourcc(*"mp4v"),
            self.fps,
            self.frame_size
        )

        # Save pre-event frames
        for frame in video_buffer.get_frames():
            writer.write(frame)

        # Save post-event frames
        total_frames = post_seconds * self.fps

        for _ in range(total_frames):
            frame = camera_manager.get_frame()
            if frame is not None:
                writer.write(frame)

            time.sleep(1 / self.fps)

        writer.release()

        # Save audio
        audio = audio_buffer.get_audio()

        sf.write(
            temp_audio,
            audio,
            44100
        )

        # Merge audio and video
        subprocess.run(
            [
                FFMPEG_PATH,
                "-y",

                "-i",
                temp_video,

                "-i",
                temp_audio,

                "-c:v",
                "libx264",

                "-preset",
                "ultrafast",

                "-pix_fmt",
                "yuv420p",

                "-r",
                "20",

                "-c:a",
                "aac",

                final_video
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Cleanup temporary files
        if os.path.exists(temp_video):
            os.remove(temp_video)

        if os.path.exists(temp_audio):
            os.remove(temp_audio)

        print("✅ Evidence Saved")

        return final_video

    def record_async(
        self,
        event_folder,
        callback=None,
        post_seconds=10
    ):

        def worker():

            video = self.record(
                event_folder=event_folder,
                post_seconds=post_seconds
            )

            if callback:
                callback(video)

        thread = threading.Thread(
            target=worker,
            daemon=True
        )

        thread.start()

        return thread


evidence_recorder = EvidenceRecorder()