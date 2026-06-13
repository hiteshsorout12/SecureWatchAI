from socket_manager import socketio


def _emit(event_name, payload):
    """
    Internal helper for emitting Socket.IO events.
    """

    try:
        if getattr(socketio, "server", None) is None:
            print("⚠️ SocketIO not running.")
            return False
        
        print(f"📡 Emitting: {event_name}")
        socketio.emit(event_name, payload)
        return True

    except Exception as e:
        print(f"⚠️ Socket emit failed: {e}")
        return False


# -----------------------------
# Existing Function (unchanged)
# -----------------------------
def send_live_alert(title, message, level="info"):

    return _emit(
        "security_alert",
        {
            "title": title,
            "message": message,
            "level": level
        }
    )


# -----------------------------
# New Generic Publishers
# -----------------------------
def publish_event(event):

    return _emit(
        "security_event",
        event
    )


def publish_evidence(evidence):

    return _emit(
        "new_evidence",
        evidence
    )


def publish_risk(risk):

    return _emit(
        "risk_update",
        risk
    )


def publish_device_status(status):

    return _emit(
        "device_status",
        status
    )


def publish_notification(notification):

    return _emit(
        "notification",
        notification
    )


def publish_audio_status(audio):

    return _emit(
        "audio_status",
        audio
    )
    
def publish_analytics():

    return _emit(
        "analytics_update",
        {}
    )
    
def publish_timeline():

    return _emit(
        "timeline_update",
        {}
    )
    
def publish_emergency(active):

    return _emit(
        "emergency_update",
        {
            "active": active
        }
    )