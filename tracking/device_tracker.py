import time
import asyncio

from location.ip_location import get_location

from services.location_history_service import (
    save_location_history
)

from location.windows_location import (
    get_windows_location
)

from services.device_status_service import (
    update_device_status
)

DEVICE_NAME = "SecureWatch-Laptop"

while True:

    try:

        ip_location = get_location()

        gps_location = asyncio.run(
            get_windows_location()
        )

        update_device_status(
            device_name=DEVICE_NAME,

            ip_address=ip_location["ip"],

            city=ip_location["city"],

            country=ip_location["country"],

            latitude=str(
                gps_location["latitude"]
            ),

            longitude=str(
                gps_location["longitude"]
            )
        )

        save_location_history(
            DEVICE_NAME,
            str(gps_location["latitude"]),
            str(gps_location["longitude"])
        )

        print(
            "Device Updated:"
        )

        print(
            "IP:",
            ip_location["ip"]
        )

        print(
            "City:",
            ip_location["city"]
        )

        print(
            "Country:",
            ip_location["country"]
        )

        print(
            "Latitude:",
            gps_location["latitude"]
        )

        print(
            "Longitude:",
            gps_location["longitude"]
        )

    except Exception as e:

        print(
            "Tracker Error:",
            e
        )

    time.sleep(30)