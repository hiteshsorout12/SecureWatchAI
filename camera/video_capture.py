import cv2
FFMPEG_PATH = r"C:\Users\hitesh\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"
import subprocess
import os

from datetime import datetime


def record_video(seconds=5):

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    if not cap.isOpened():

        print(
            "Camera Not Available"
        )

        return None

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    temp_video = (
        f"evidence/videos/{timestamp}_temp.mp4"
    )

    final_video = (
        f"evidence/videos/{timestamp}.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(
        *'mp4v'
    )

    out = cv2.VideoWriter(
        temp_video,
        fourcc,
        20.0,
        (640, 480)
    )

    total_frames = seconds * 20

    for _ in range(total_frames):

        ret, frame = cap.read()

        if not ret:
            break

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    del cap
    del out

    print(
        "Converting Video..."
    )

    try:

        subprocess.run(
            [
                FFMPEG_PATH,
                "-y",
                "-i",
                temp_video,
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                final_video
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        os.remove(
            temp_video
        )

        print(
            "Video Saved:",
            final_video
        )

        return final_video

    except Exception as e:

        print(
            "FFmpeg Conversion Failed:",
            e
        )

        return temp_video


if __name__ == "__main__":

    record_video(5)