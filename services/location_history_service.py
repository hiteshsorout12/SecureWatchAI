from sqlalchemy.orm import sessionmaker

from database.connection import engine

from models.location_history import (
    LocationHistory
)

Session = sessionmaker(
    bind=engine
)


def save_location_history(
        device_name,
        latitude,
        longitude):

    session = Session()

    location = LocationHistory(
        device_name=device_name,
        latitude=latitude,
        longitude=longitude
    )

    session.add(location)

    session.commit()

    session.close()

    print("Location Saved")