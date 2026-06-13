import time
import os
import cv2

from datetime import datetime

from camera.camera_service import open_camera


def capture_with_retry(

    max_attempts=3,

    delay=1

):

    camera = open_camera()

    if camera is None:

        print(
            "❌ Camera Not Available"
        )

        return None

    try:

        for attempt in range(

            1,

            max_attempts + 1

        ):

            print(

                f"📸 Capture Attempt {attempt}"

            )

            time.sleep(
                delay
            )

            frame = camera.get_frame()

            if frame is None:

                continue

            filename = (

                datetime.now().strftime(

                    "%Y%m%d_%H%M%S"

                )

                + ".jpg"

            )

            photo_path = os.path.join(

                "evidence",

                "photos",

                filename

            )

            cv2.imwrite(

                photo_path,

                frame

            )

            print(

                "✅ Photo Captured:",

                photo_path

            )

            return photo_path

        print(

            "❌ Failed after retries"

        )

        return None

    finally:

        camera.stop()