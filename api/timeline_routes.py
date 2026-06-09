from flask import Blueprint, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

from database.connection import engine
from models.audit_log import AuditLog

timeline_bp = Blueprint(
    "timeline",
    __name__
)

Session = sessionmaker(bind=engine)


@timeline_bp.route(
    "/dashboard/timeline",
    methods=["GET"]
)
def get_timeline():

    session = Session()

    try:

        logs = (
            session.query(AuditLog)
            .order_by(
                desc(AuditLog.created_at)
            )
            .limit(20)
            .all()
        )

        result = []

        for log in logs:

            result.append({

                "time": log.created_at.strftime(
                    "%I:%M:%S %p"
                ),

                "action": log.action,

                "module": log.module,

                "details": log.details,

                "status": log.status

            })

        return jsonify(result)

    finally:

        session.close()