from flask import Blueprint
from flask import send_file
from flask import jsonify

import os

image_bp = Blueprint(
    "image",
    __name__
)


@image_bp.route(
    "/image/<path:image_path>"
)
def get_image(image_path):

    if not os.path.exists(image_path):

        return jsonify({
            "error": "Image not found"
        }), 404

    return send_file(
        image_path,
        mimetype="image/jpeg"
    )


@image_bp.route(
    "/video/<path:video_path>"
)
def get_video(video_path):

    if not os.path.exists(video_path):

        return jsonify({
            "error": "Video not found"
        }), 404

    return send_file(
        video_path,
        mimetype="video/mp4"
    )
@image_bp.route("/audio/<path:audio_path>")
def get_audio(audio_path):

    if not os.path.exists(audio_path):

        return jsonify({
            "error": "Audio not found"
        }), 404

    return send_file(
        audio_path,
        mimetype="audio/wav"
    )