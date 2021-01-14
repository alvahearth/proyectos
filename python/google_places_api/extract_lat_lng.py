from urllib.parse import urlencode, parse_qsl
from urllib.request import urlopen
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

def extract_lat_lng(address):

    service_url = "https://maps.googleapis.com/maps/api/geocode/json"
    url = urlencode({"address":address,"key":api_key})
    final_url = f"{service_url}?{url}"
    
    file_to_edit = urlopen(final_url)
    dh = file_to_edit.read().decode()
    js = json.loads(dh)
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    
    return lat,lng

user_input = input("Enter a valid address: ")
result = extract_lat_lng(user_input)
print(result)
