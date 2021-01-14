import urllib.request
import urllib.parse
import urllib.error
import json

api_key = "AIzaSyDw52dbm_ff_155vkfZw96QcdcdSCp1540"

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    
while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({"address": address,"key":api_key})
    
    ue = urllib.request.urlopen(url)
    data = ue.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None
    
    #if not js or "status" not in js or "status" is not "OK":
        # print("Could not retrieve data")
        #break
    
    
    lat =  js["results"][0]["geometry"]["location"]["lat"]
    lng =  js["results"][0]["geometry"]["location"]["lng"]
    print("Latitude:",lat)
    print("Longitude:",lng)