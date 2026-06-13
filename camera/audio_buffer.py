from collections import deque
import threading

import numpy as np
import sounddevice as sd


class AudioBuffer:

    def __init__(

        self,

        seconds=5,

        sample_rate=44100,

        channels=1

    ):

        self.sample_rate = sample_rate

        self.channels = channels

        self.max_samples = seconds * sample_rate

        self.buffer = deque(maxlen=self.max_samples)

        self.running = False

        self.stream = None

        self.lock = threading.Lock()

    # ----------------------------
    # Audio Callback
    # ----------------------------

    def callback(

        self,

        indata,

        frames,

        time,

        status

    ):

        if status:
            if status.input_overflow:
                return
            print(status)

        with self.lock:

            self.buffer.extend(

                indata.copy().flatten()

            )

    # ----------------------------
    # Start
    # ----------------------------

    def start(self):

        if self.running:

            return

        self.running = True

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            blocksize=1024,
            callback=self.callback
        )

        self.stream.start()

        print("🎤 Audio Buffer Started")

    # ----------------------------
    # Stop
    # ----------------------------

    def stop(self):

        self.running = False

        if self.stream:

            self.stream.stop()

            self.stream.close()

        print("🎤 Audio Buffer Stopped")

    # ----------------------------
    # Get Audio
    # ----------------------------

    def get_audio(self):

        with self.lock:

            return np.array(

                self.buffer,

                dtype=np.float32

            )


audio_buffer = AudioBuffer()