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
    "/device/location-history",
    methods=["GET"]
)
def get_location_history():

    session = Session()

    locations = (
        session.query(LocationHistory)
        .order_by(
            desc(LocationHistory.timestamp)
        )
        .limit(50)
        .all()
    )

    result = []

    for location in locations:

        result.append(
            {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "timestamp": str(
                    location.timestamp
                )
            }
        )

    return result