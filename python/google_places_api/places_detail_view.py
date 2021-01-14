from urllib.parse import urlencode
from urllib.request import urlopen
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

service_url = "https://maps.googleapis.com/maps/api/place/details/json"

params = {
    "key": api_key,
    "place_id":"ChIJIV28eyzOYpYRZ-J_J24vstM",
    "fields":"name,rating,formatted_phone_number",
}

params_encoded = urlencode(params)

final_url = f"{service_url}?{params_encoded}"



print(final_url)
