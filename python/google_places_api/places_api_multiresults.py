from urllib.parse import urlencode
from urllib.request import urlopen
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

service_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

lat = -33.4661458
lng = -70.580714
radius = 9000

params = {
    "key": api_key,
    "location": f"{lat},{lng}",
    "radius": radius,
    "keyword": "casa",
}

params_encoded = urlencode(params)

final_url = f"{service_url}?{params_encoded}"

print(final_url)