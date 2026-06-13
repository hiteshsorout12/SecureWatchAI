from camera.audio_manager import audio_manager


class AudioRecorder:

    def start(self, filename):

        self.filename = filename

        audio_manager.start()

        print("🎤 Audio Recording Started")

    def stop(self):

        audio_manager.stop(self.filename)

        print("🎤 Audio Recording Stopped")


audio_recorder = AudioRecorder()