from flask import Blueprint

from services.socket_service import send_live_alert

socket_test_bp = Blueprint(
    "socket_test",
    __name__
)


@socket_test_bp.route(
    "/socket/test",
    methods=["GET"]
)
def socket_test():

    send_live_alert(
        title="🚀 SecureWatch Live",
        message="Socket.IO is working successfully!",
        level="success"
    )

    return {
        "status": "success",
        "message": "Notification sent"
    }