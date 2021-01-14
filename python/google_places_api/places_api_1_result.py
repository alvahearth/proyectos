from urllib.request import urlopen
from urllib.parse import urlencode,parse_qsl
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

# returns a single valid adrress

service_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

lat = -33.4661458
lng = -70.580714
radius = 5000

params = {
    "key": api_key,
    "input":"restaurant",
    "inputtype":"textquery",
    "fields":"formatted_address,geometry,place_id",
    "locationbias": f"circle:{radius}@{lat},{lng}",
}

params_encoded = urlencode(params)

final_url = f"{service_url}?{params_encoded}"

print(final_url)





