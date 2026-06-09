import os


def remote_lock():

    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )

    return {
        "message": "Device Locked"
    }