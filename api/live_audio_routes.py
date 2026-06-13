from flask import Blueprint

from camera.live_audio import live_audio


live_audio_bp = Blueprint(
    "live_audio",
    __name__
)


@live_audio_bp.route(
    "/audio/start",
    methods=["POST"]
)
def start_audio():

    live_audio.start()

    return {
        "success": True,
        "message": "Live audio started"
    }


@live_audio_bp.route(
    "/audio/stop",
    methods=["POST"]
)
def stop_audio():

    live_audio.stop()

    return {
        "success": True,
        "message": "Live audio stopped"
    }