import sounddevice as sd
import soundfile as sf
import threading
import numpy as np

class AudioManager:

    def __init__(self):

        self.sample_rate = 44100
        self.channels = 1

        self.recording = False

        self.frames = []

        self.stream = None

    # --------------------------
    # Audio Callback
    # --------------------------

    def callback(self, indata, frames, time, status):

        if self.recording:

            self.frames.append(indata.copy())

    # --------------------------
    # Start Recording
    # --------------------------

    def start(self):

        if self.recording:
            return

        print("🎤 Audio Recording Started")

        self.frames = []

        self.recording = True

        self.stream = sd.InputStream(

            samplerate=self.sample_rate,

            channels=self.channels,

            callback=self.callback

        )

        self.stream.start()

    # --------------------------
    # Stop Recording
    # --------------------------

    def stop(self, filename):

        if not self.recording:
            return

        self.recording = False

        self.stream.stop()

        self.stream.close()

        audio = np.concatenate(self.frames, axis=0)
        sf.write(
            filename,
            audio,
            self.sample_rate
        )

        print("🎤 Audio Saved")


audio_manager = AudioManager()