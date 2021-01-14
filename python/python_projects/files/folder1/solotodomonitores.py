import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://www.solotodo.cl/monitors?refresh_rate_start=110648")

page = url.read()
url.close()

soup = BeautifulSoup(page,"html.parser")

containers = soup.findAll("div",{"class":"d-flex flex-column category-browse-result"})



for container in containers:
    prodruct_name = container.find("h3")
    name = prodruct_name.text
    name = name.strip()

    product_price = container.find("div",{"class":"price flex-grow"})
    price = product_price.text

    product_specs = container.find("div",{"class":"description-container"})
    specs = product_specs.dl.text
    specs = specs.strip()
    print("\n",name,"|",price,"|",specs)


