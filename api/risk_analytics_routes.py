from flask import Blueprint
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from database.connection import engine
from models.event import Event

risk_analytics_bp = Blueprint(
    "risk_analytics",
    __name__
)

Session = sessionmaker(bind=engine)


@risk_analytics_bp.route(
    "/analytics/risk",
    methods=["GET"]
)
def risk_analytics():

    session = Session()

    try:

        high_risk = (
            session.query(Event)
            .filter(Event.status == "HIGH")
            .count()
        )

        medium_risk = (
            session.query(Event)
            .filter(Event.status == "MEDIUM")
            .count()
        )

        low_risk = (
            session.query(Event)
            .filter(Event.status == "LOW")
            .count()
        )

        average_risk = (
            session.query(
                func.avg(Event.risk_score)
            )
            .scalar()
        )

        return {
            "high_risk": high_risk,
            "medium_risk": medium_risk,
            "low_risk": low_risk,
            "average_risk": round(
                average_risk or 0,
                2
            )
        }

    finally:
        session.close()