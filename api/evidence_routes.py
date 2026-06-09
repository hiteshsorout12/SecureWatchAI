from flask import Blueprint
from flask import jsonify
from flask import request

from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence

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