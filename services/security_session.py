from camera.video_buffer import video_buffer
from camera.audio_buffer import audio_buffer


class SecuritySession:

    def __init__(self):

        self.active = False

    def start(self):

        if self.active:
            return

        print("🚨 Security Session Started")

        video_buffer.start()
        audio_buffer.start()

        self.active = True

    def stop(self):

        if not self.active:
            return

        print("✅ Security Session Ended")

        video_buffer.stop()
        audio_buffer.stop()

        self.active = False

    def is_active(self):

        return self.active


security_session = SecuritySession()