import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen(
    "https://www.sony.cl/electronics/videocamaras/t/camara-de-video-handycam"
)

page_html = url.read()
url.close()

soup = BeautifulSoup(page_html, "html.parser")

containers = soup.findAll("div", {"class": "gallery-item-inner"})

filename = "sony.csv"
f = open(filename, "w")

headers = "Product name, Price,\n"

f.write(headers)


for container in containers:
    product_name = container.findAll("div", {"class": "product-name p2"})
    name = product_name[0].text

    product_price = container.findAll("span", {"class": "price p2"})
    try:
        price = product_price[0].text
        if len(price) < 1:
            price = "No price"
    except:
        price = "No price listed"
    print(name, "|", price)

    f.write(name + "," + price + "\n")

f.close()

