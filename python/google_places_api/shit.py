from urllib.request import urlopen
from urllib.parse import urlencode
import json
api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

service_url = "https://maps.googleapis.com/maps/api/place/details/json"

params = {
    "key":api_key,
    "place_id":"ChIJMzxtptXPYpYRI6I9WdV9PAY",
    "fields":"formatted_address,name,geometry"
}

encoded_params = urlencode(params)

final_url = f"{service_url}?{encoded_params}"

print(final_url)