import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://www.pcfactory.cl/monitores?categoria=995&papa=256")

page_html = url.read()
url.close

soup = BeautifulSoup(page_html,"html.parser")

containers = soup.findAll("div",{"class":"wrap-caluga-matrix"})


#container = containers[0]

for container in containers:
    product_name = container.findAll("span",{"class":"nombre"})
    name = product_name[0].text

    product_price = container.findAll("span",{"class":"txt-precio"})
    price = product_price[0].text
    price = price.replace(" ","")

    product_brand = container.findAll("span",{"class":"marca"})
    brand = product_brand[0].text[0:-2]
    brand = brand.replace(" ","")

    print(name,"|",price,"|",brand)