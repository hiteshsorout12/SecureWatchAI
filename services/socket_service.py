from socket_manager import socketio


def send_live_alert(
        title,
        message,
        level="info"
):

    socketio.emit(
        "security_alert",
        {
            "title": title,
            "message": message,
            "level": level
        }
    )