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


@remote_bp.route(
    "/remote/capture",
    methods=["POST"]
)
def capture_now():

    result = remote_capture()

    return result

@remote_bp.route(
    "/remote/alarm",
    methods=["POST"]
)
def alarm_now():

    result = remote_alarm()

    return result

@remote_bp.route(
    "/remote/lock",
    methods=["POST"]
)
def lock_now():

    result = remote_lock()

    return result