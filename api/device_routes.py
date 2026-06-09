from flask import Blueprint
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.device_status import DeviceStatus

device_bp = Blueprint(
    "device",
    __name__
)

Session = sessionmaker(bind=engine)


@device_bp.route(
    "/device/status",
    methods=["GET"]
)
def get_device_status():

    session = Session()

    try:

        device = (
            session.query(DeviceStatus)
            .order_by(
                desc(DeviceStatus.last_seen)
            )
            .first()
        )

        if not device:

            return {
                "message": "No Device Found"
            }

        latitude = ""
        longitude = ""

        try:

            latitude = round(
                float(device.latitude),
                6
            )

            longitude = round(
                float(device.longitude),
                6
            )

        except:

            latitude = device.latitude
            longitude = device.longitude

        return {
            "device_name": device.device_name,
            "status": device.status,
            "ip_address": device.ip_address,
            "city": device.city,
            "country": device.country,
            "latitude": latitude,
            "longitude": longitude,
            "last_seen": str(device.last_seen)
        }

    finally:
        session.close()