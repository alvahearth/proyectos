from urllib.parse import urlencode, parse_qsl
from urllib.request import urlopen
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

class GoogleClient(object):
    lat = None
    lng = None
    data_type = "json"
    location_query = None
    api_key = None
    
    def __init__(self,api_key=None,address_or_postal_code=None,*args, **kwargs):
        super().__init__(*args,**kwargs)
        if api_key == None:
            raise Exception("API key is needed")
        self.api_key = api_key
        self.location_query = address_or_postal_code
        if self.location_query != None:
            self.extract_lat_lng()
                
    def extract_lat_lng(self):

        service_url = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        url = urlencode({"address":self.location_query,"key":self.api_key})
        final_url = f"{service_url}?{url}"
    
        file_to_edit = urlopen(final_url)
        dh = file_to_edit.read().decode()
        js = json.loads(dh)
    
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        
        self.lat = lat
        self.lng = lng
        return lat,lng
    
    def detail_view(self,place_id="ChIJIV28eyzOYpYRZ-J_J24vstM"):
        
        service_url = f"https://maps.googleapis.com/maps/api/place/details/json"

        params = {
            "place_id": f"{place_id}",
            "fields":"name,rating,formatted_phone_number",
            "key": self.api_key,
        }

        params_encoded = urlencode(params)

        final_url = f"{service_url}?{params_encoded}"
        
        file_to_edit = urlopen(final_url)
        dh = file_to_edit.read().decode()
        js = json.loads(dh)
        
        return js
        

client = GoogleClient.detail_view(place_id="ChIJIV28eyzOYpYRZ-J_J24vstM")

print(client)