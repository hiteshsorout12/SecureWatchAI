import sounddevice as sd
import threading

from socket_manager import socketio


class LiveAudio:

    def __init__(self):

        self.running = False
        self.stream = None

        self.sample_rate = 16000
        self.channels = 1

    def callback(
        self,
        indata,
        frames,
        time,
        status
    ):

        if not self.running:
            return

        socketio.emit(
            "live_audio",
            indata.copy().tobytes()
        )

    def start(self):

        if self.running:
            return

        self.running = True

        self.stream = sd.InputStream(

            samplerate=self.sample_rate,

            channels=self.channels,

            dtype="int16",

            callback=self.callback

        )

        self.stream.start()

        print("🎤 Live Audio Started")

    def stop(self):

        if not self.running:
            return

        self.running = False

        self.stream.stop()
        self.stream.close()

        print("🛑 Live Audio Stopped")


live_audio = LiveAudio()