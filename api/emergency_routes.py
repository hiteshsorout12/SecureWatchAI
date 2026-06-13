from flask import Blueprint

from services.security_session_service import get_active_session
from services.security_session_service import start_session
from services.security_session_service import end_session
from services.emergency_manager import emergency_manager

from camera.stream import start_camera, stop_camera
from camera.audio_manager import audio_manager

from services.socket_service import (
    send_live_alert,
    publish_device_status,
    publish_emergency
)

emergency_bp = Blueprint(
    "emergency",
    __name__
)


@emergency_bp.route(
    "/emergency/status",
    methods=["GET"]
)
def emergency_status():

    session = get_active_session()

    if session is None:

        return {
            "active": False
        }

    return {

        "active": session.active,

        "session_type": session.session_type,

        "status": session.status,

        "risk_score": session.risk_score,

        "camera": session.camera_on,

        "microphone": session.microphone_on,

        "live_stream": session.live_stream_on,

        "owner_connected": session.owner_connected

    }
    
@emergency_bp.route(
    "/emergency/start",
    methods=["POST"]
)
def start_emergency():

    session = start_session(
        session_type="MANUAL",
        risk_score=0,
        status="MANUAL"
    )

    emergency_manager.start()

    start_camera()

    audio_manager.start()
    publish_emergency(True) 
    
    send_live_alert(
        title="🚨 Emergency Started",
        message="Emergency mode activated.",
        level="danger"
    )
    publish_device_status({
        "status": "EMERGENCY"
    })

    return {
        "success": True,
        "session_id": session.id,
        "message": "Emergency Started"
    }
    
@emergency_bp.route(
    "/emergency/end",
    methods=["POST"]
)
def end_emergency():

    end_session()

    emergency_manager.stop()

    stop_camera()

    audio_manager.stop(
        "evidence/manual_audio.wav"
    )
    publish_emergency(False)  
    send_live_alert(
        title="✅ Emergency Ended",
        message="Monitoring resumed.",
        level="success"
    )

    publish_device_status({
        "status": "ONLINE"
    })

    return {
        "success": True,
        "message": "Emergency Ended"
    }