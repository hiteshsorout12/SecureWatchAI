import winsound


def remote_alarm():

    for _ in range(5):

        winsound.Beep(
            2500,
            1000
        )

    return {
        "message": "Alarm Activated"
    }