from flask import Blueprint
from flask import request
from flask import jsonify

settings_bp = Blueprint(
    "settings",
    __name__
)

# Temporary in-memory settings
settings = {
    "startup": True,
    "notifications": True,
    "email_alerts": True,
    "alarm_sound": True,
    "email": "owner@example.com"
}


# -----------------------------
# Get Settings
# -----------------------------
@settings_bp.route(
    "/api/settings",
    methods=["GET"]
)
def get_settings():

    return jsonify(settings)


# -----------------------------
# Save Settings
# -----------------------------
@settings_bp.route(
    "/settings",
    methods=["POST"]
)
def save_settings():

    data = request.get_json()

    settings["startup"] = data.get(
        "startup",
        True
    )

    settings["notifications"] = data.get(
        "notifications",
        True
    )

    settings["email_alerts"] = data.get(
        "email_alerts",
        True
    )

    settings["alarm_sound"] = data.get(
        "alarm_sound",
        True
    )

    return jsonify({
        "success": True,
        "message": "Settings Saved Successfully"
    })


# -----------------------------
# Change Email
# -----------------------------
@settings_bp.route(
    "/settings/email",
    methods=["POST"]
)
def change_email():

    data = request.get_json()

    settings["email"] = data.get(
        "email",
        settings["email"]
    )

    return jsonify({
        "success": True,
        "message": "Email Updated Successfully"
    })


# -----------------------------
# Reset Settings
# -----------------------------
@settings_bp.route(
    "/settings/reset",
    methods=["POST"]
)
def reset_settings():

    settings["startup"] = True
    settings["notifications"] = True
    settings["email_alerts"] = True
    settings["alarm_sound"] = True

    return jsonify({
        "success": True,
        "message": "Settings Reset Successfully"
    })