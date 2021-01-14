import urllib.request
import urllib.parse
from urllib.parse import parse_qsl
import urllib.error
import requests
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"
service_url = "https://maps.googleapis.com/maps/api/geocode/json"

address = "La Laguna 2135 Penalolen, Peñalolén Región Metropolitana"

params = urllib.parse.urlencode({"address":address,"key":api_key})

final_url = f"{service_url}?{params}"

page = urllib.request.urlopen(final_url)

url = page.read().decode()

js = json.loads(url)["results"][0]["geometry"]

lat_lng = js["location"]

location_dict = dict(lat_lng)

lat = 0
lng = 0

for k,v in location_dict.items():
    if lat == 0 and lng == 0:
        lat = v
    else:
        lng = v
        
#print(f"({lat},{lng})")

parsed_url = urllib.parse.urlparse(final_url)



new_final_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{parsed_url.query}"



base_place_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

place_params = {
    "key": api_key,
    "location": f"{lat},{lng}",
    "radius": 2000,
    "keyword" : "comida"
}

params_encoded = urllib.parse.urlencode(place_params)

places_final_url = f"{base_place_url}?{params_encoded}"

print(places_final_url)

url = urllib.request.urlopen(places_final_url)

location = url.read().decode()

js = json.loads(location)

print(js)
