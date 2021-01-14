from urllib.parse import urlencode
import requests
import json
api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

def extract_lat_long(adrress_or_postal_code, data_type = "json"):
    
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": adrress_or_postal_code, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200,299):
        return {}
    latlong = {}
    try:
        latlong = r.json()["results"][0]["geometry"]["location"]
    except:
        pass
    return latlong.get("lat"),latlong.get("lng")

print(extract_lat_long("1600 Amphitheatre Parkway, Mountain View, CA"))





