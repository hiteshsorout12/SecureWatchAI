from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.audit_log import AuditLog

audit_bp = Blueprint(
    "audit",
    __name__
)

Session = sessionmaker(bind=engine)


@audit_bp.route("/audit-logs", methods=["GET"])
def get_audit_logs():

    session = Session()

    logs = session.query(AuditLog).all()

    result = []

    for log in logs:

        result.append({
            "id": log.id,
            "action": log.action,
            "module": log.module,
            "details": log.details,
            "status": log.status
        })

    session.close()

    return jsonify(result)


@audit_bp.route("/audit-logs", methods=["POST"])
def create_audit_log():

    data = request.get_json()

    session = Session()

    log = AuditLog(
        action=data["action"],
        module=data["module"],
        details=data["details"],
        status=data["status"]
    )

    session.add(log)
    session.commit()

    session.close()

    return jsonify({
        "message": "Audit Log Created Successfully"
    })