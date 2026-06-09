from flask import Blueprint
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.event import Event

dashboard_alerts_bp = Blueprint(
    "dashboard_alerts",
    __name__
)

Session = sessionmaker(bind=engine)


@dashboard_alerts_bp.route(
    "/dashboard/alerts",
    methods=["GET"]
)
def get_dashboard_alerts():

    session = Session()

    try:

        events = (
            session.query(Event)
            .order_by(
                desc(Event.id)
            )
            .limit(5)
            .all()
        )

        return [
            {
                "event_type": event.event_type,
                "risk_score": event.risk_score,
                "status": event.status
            }
            for event in events
        ]

    finally:
        session.close()