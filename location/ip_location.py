import requests


def get_location():

    response = requests.get(
        "http://ip-api.com/json/"
    )

    data = response.json()

    return {
        "ip": data.get("query"),
        "city": data.get("city"),
        "region": data.get("regionName"),
        "country": data.get("country")
    }