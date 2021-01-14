import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://www.zmart.cl/JuegosPS4")

page_html = url.read()
url.close()

soup = BeautifulSoup(page_html, "html.parser")

containers = soup.findAll("div", {"class": "BoxProductoS2 BorderPlatPS4"})

filename = "zmart.csv"
f = open(filename, "w")

headers = "Name,Price,\n"

f.write(headers)

for container in containers:
    product_name = container.findAll("div", {"class": "BoxProductoS2_Descripcion"})
    name = product_name[0].text
    name = name.replace("", "")
    name = name.replace(",", " ")

    product_price = container.findAll("span", {"class": "BoxProductoS2_Precio"})
    price = product_price[0].text
    print(name, "|", price)

    f.write(name + "," + price + "\n")

f.close()
