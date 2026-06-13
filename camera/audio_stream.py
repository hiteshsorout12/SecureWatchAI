import sounddevice as sd

devices = sd.query_devices()

print("\n===== AUDIO DEVICES =====\n")

for index, device in enumerate(devices):

    print(f"{index}: {device['name']}")

print("\n=========================\n")