from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.device_status import DeviceStatus

Session = sessionmaker(bind=engine)


def update_device_status(
        device_name,
        ip_address,
        city,
        country,
        latitude="",
        longitude="",
        wifi_name="",
        battery_percent=""):

    session = Session()

    device = DeviceStatus(

        device_name=device_name,

        ip_address=ip_address,

        city=city,

        country=country,

        latitude=latitude,

        longitude=longitude,

        wifi_name=wifi_name,

        battery_percent=battery_percent,

        status="ONLINE"
    )

    session.add(device)

    session.commit()

    session.close()

    print("Device Status Updated")