from flask import Blueprint
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.location_history import LocationHistory

location_bp = Blueprint(
    "location",
    __name__
)

Session = sessionmaker(
    bind=engine
)

@location_bp.route(
    "/api/location",
    methods=["GET"]
)
def get_current_location():

    session = Session()

    location = (
        session.query(LocationHistory)
        .order_by(
            desc(LocationHistory.timestamp)
        )
        .first()
    )

    if not location:

        return {
            "success": False
        },404

    return {
        "device_name": location.device_name,

        "latitude": location.latitude,

        "longitude": location.longitude,

        "city": "Unknown",

        "country": "Unknown",

        "accuracy": "GPS",

        "timestamp": str(location.timestamp)

    }