from flask import Flask
from flask_cors import CORS
from flask import send_from_directory
from flask import send_file

from api.audit_routes import audit_bp
from api.alert_routes import alert_bp
from api.evidence_routes import evidence_bp
from api.event_routes import event_bp
from api.user_routes import user_bp
from api.remote_routes import remote_bp
from api.device_routes import device_bp
from api.location_routes import location_bp
from api.latest_evidence_routes import latest_evidence_bp
from api.image_routes import image_bp
from api.evidence_gallery_routes import gallery_bp
from api.analytics_routes import analytics_bp
from api.risk_analytics_routes import risk_analytics_bp
from api.dashboard_alert_routes import dashboard_alerts_bp
from api.timeline_routes import timeline_bp

from database.connection import engine
from database.base import Base

from models.device_status import DeviceStatus
from models.evidence import Evidence
from models.alert import Alert
from models.health_status import HealthStatus
from models.event import Event
from models.user import User
from models.face_profile import FaceProfile
from models.risk_assessment import RiskAssessment
from models.audit_log import AuditLog
from models.location_history import LocationHistory
from models.location_history import (
    LocationHistory
)

from socket_manager import socketio

# Create tables
Base.metadata.create_all(bind=engine)

print("All Tables Created")

# Flask App
app = Flask(__name__)

CORS(app)

socketio.init_app(
    app,
    cors_allowed_origins="*"
)


@app.route("/")
def home():

    return send_from_directory(
        "dashboard/frontend",
        "index.html"
    )

@app.route("/evidence")
def evidence_page():

    return send_from_directory(
        "dashboard/frontend",
        "evidence.html"
    )


@app.route("/location")
def location_page():

    return send_from_directory(
        "dashboard/frontend",
        "location.html"
    )
    
@app.route("/history")
def history_page():

    return send_from_directory(
        "dashboard/frontend",
        "history.html"
    )


@app.route("/style.css")
def css():

    return send_from_directory(
        "dashboard/frontend",
        "style.css"
    )


@app.route("/app.js")
def app_js():

    return send_from_directory(
        "dashboard/frontend",
        "app.js"
    )


@app.route("/evidence.js")
def evidence_js():

    return send_from_directory(
        "dashboard/frontend",
        "evidence.js"
    )


@app.route("/location.js")
def location_js():

    return send_from_directory(
        "dashboard/frontend",
        "location.js"
    )
    
@app.route("/history.js")
def history_js():

    return send_from_directory(
        "dashboard/frontend",
        "history.js"
    )
    
@app.route("/history.css")
def history_css():

    return send_from_directory(
        "dashboard/frontend",
        "history.css"
    )


@app.route("/evidence/photos/<filename>")
def serve_photo(filename):

    return send_from_directory(
        "evidence/photos",
        filename
    )


@app.route("/evidence/videos/<filename>")
def serve_video(filename):

    return send_from_directory(
        "evidence/videos",
        filename
    )
    
@app.route("/manifest.json")
def manifest():

    return send_from_directory(
        "dashboard/frontend",
        "manifest.json"
    )
    
@app.route("/favicon.ico")
def favicon():

    return send_from_directory(
        "dashboard/frontend",
        "favicon.ico"
    )
    
# Register Blueprints
app.register_blueprint(alert_bp)
app.register_blueprint(evidence_bp)
app.register_blueprint(user_bp)
app.register_blueprint(event_bp)
app.register_blueprint(audit_bp)
app.register_blueprint(device_bp)
app.register_blueprint(remote_bp)
app.register_blueprint(location_bp)
app.register_blueprint(latest_evidence_bp)
app.register_blueprint(image_bp)
app.register_blueprint(gallery_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(risk_analytics_bp)
app.register_blueprint(dashboard_alerts_bp)
app.register_blueprint(timeline_bp)

socketio.run(
    app,
    host="0.0.0.0",
    port=5000,
    debug=True,
    allow_unsafe_werkzeug=True
)
