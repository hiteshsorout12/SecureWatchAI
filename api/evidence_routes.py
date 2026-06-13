from flask import Blueprint
from flask import jsonify
from flask import request

from models.audit_log import AuditLog
from models.alert import Alert
from models.risk_assessment import RiskAssessment
from models.security_session import SecuritySession

import shutil
import os

from sqlalchemy import delete

from models.event import Event

from flask import send_file
import tempfile

from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence

from services.socket_service import (
    publish_analytics,
    publish_timeline,
    publish_device_status,
    send_live_alert
)

evidence_bp = Blueprint(
    "evidence",
    __name__
)

Session = sessionmaker(bind=engine)


@evidence_bp.route("/evidence", methods=["GET"])
def get_evidence():

    session = Session()

    evidence_list = session.query(Evidence).all()

    result = []

    for evidence in evidence_list:

        result.append({
            "id": evidence.id,
            "event_id": evidence.event_id,
            "photo_path": evidence.photo_path,
            "video_path": evidence.video_path,
            "audio_path": evidence.audio_path
        })

    session.close()

    return jsonify(result)


@evidence_bp.route("/evidence", methods=["POST"])
def create_evidence():

    data = request.get_json()

    session = Session()

    evidence = Evidence(
        event_id=data["event_id"],
        photo_path=data["photo_path"],
        video_path=data["video_path"],
        audio_path=data["audio_path"]
    )

    session.add(evidence)
    session.commit()

    session.close()

    return jsonify({
        "message": "Evidence Created Successfully"
    })
    
@evidence_bp.route(
    "/evidence/download/<event_id>",
    methods=["GET"]
)
def download_event(event_id):

    session = Session()

    try:

        evidence = session.query(Evidence).filter(
            Evidence.event_id == event_id
        ).first()

        if not evidence:

            return jsonify({
                "error": "Evidence not found"
            }), 404

        temp_dir = tempfile.mkdtemp()

        if evidence.photo_path and os.path.exists(evidence.photo_path):
            shutil.copy(
                evidence.photo_path,
                temp_dir
            )

        if evidence.video_path and os.path.exists(evidence.video_path):
            shutil.copy(
                evidence.video_path,
                temp_dir
            )

        if evidence.audio_path and os.path.exists(evidence.audio_path):
            shutil.copy(
                evidence.audio_path,
                temp_dir
            )

        zip_path = shutil.make_archive(
            temp_dir,
            "zip",
            temp_dir
        )

        return send_file(
            zip_path,
            as_attachment=True,
            download_name=f"{event_id}.zip"
        )

    finally:

        session.close()
        
@evidence_bp.route(
    "/evidence/clear",
    methods=["DELETE"]
)
def clear_evidence():

    session = Session()

    try:

        # -----------------------------
        # Clear Database
        # -----------------------------

        session.query(Evidence).delete()

        session.query(Event).delete()

        session.query(Alert).delete()

        session.query(AuditLog).delete()

        session.query(RiskAssessment).delete()

        session.query(SecuritySession).delete()

        session.commit()

        # -----------------------------
        # Delete Evidence Files
        # -----------------------------

        folder = "evidence/events"

        if os.path.exists(folder):

            shutil.rmtree(folder)

        os.makedirs(
            folder,
            exist_ok=True
        )

        # -----------------------------
        # Refresh Dashboard
        # -----------------------------

        publish_analytics()

        publish_timeline()

        publish_device_status({

            "status": "ONLINE"

        })

        send_live_alert(

            title="🗑 Evidence Cleared",

            message="All evidence, events, alerts and timeline have been removed.",

            level="warning"

        )

        # -----------------------------
        # Response
        # -----------------------------

        return jsonify({

            "success": True,

            "message": "All Evidence Cleared Successfully"

        })

    except Exception as e:

        session.rollback()

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500

    finally:

        session.close()