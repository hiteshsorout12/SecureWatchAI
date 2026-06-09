import random


def get_random_challenge():

    challenges = [
        "BLINK",
        "LOOK_LEFT",
        "LOOK_RIGHT"
    ]

    return random.choice(
        challenges
    )