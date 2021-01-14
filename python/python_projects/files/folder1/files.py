from urllib.parse import urlencode
import requests
import json
api_key = "AIzaSyAX8u02QPF9y1cJhggJ2fgpQI6pmziSon0"


def extract_lat_long(address_or_postalcode, data_type="json"):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {
        "address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    try:
        latlng = r.json()["results"][0]["geometry"]["location"]
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")


print(extract_lat_long("1600 Amphitheatre Parkway, MountainView, CA"))
