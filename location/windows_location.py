import asyncio
from winsdk.windows.devices.geolocation import Geolocator


async def get_windows_location():

    locator = Geolocator()

    position = await locator.get_geoposition_async()

    return {
        "latitude": position.coordinate.point.position.latitude,
        "longitude": position.coordinate.point.position.longitude
    }


if __name__ == "__main__":

    result = asyncio.run(
        get_windows_location()
    )

    print(result)