from flask import Blueprint

from remote.capture_action import (
    remote_capture
)

from remote.lock_action import (
    remote_lock
)

remote_bp = Blueprint(
    "remote",
    __name__
)

from remote.alarm_action import (
    remote_alarm
)

from remote.panic_action import (
    remote_panic
)

@remote_bp.route("/remote/alarm", methods=["POST"])
def alarm_now():

    print("=" * 50)
    print("ALARM API HIT")
    print("=" * 50)

    result = remote_alarm()

    return result

@remote_bp.route("/remote/lock", methods=["POST"])
def lock_now():

    print("=" * 50)
    print("LOCK API HIT")
    print("=" * 50)

    result = remote_lock()

    return result

@remote_bp.route(
    "/remote/capture",
    methods=["POST"]
)
def capture_now():
    
    result = remote_capture()

    return result

@remote_bp.route(
    "/remote/panic",
    methods=["POST"]
)
def panic_now():

    print(
        "🚨 Panic Mode Requested"
    )

    return remote_panic()






