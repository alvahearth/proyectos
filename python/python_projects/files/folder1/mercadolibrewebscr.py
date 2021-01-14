import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen(
    "https://listado.mercadolibre.cl/notebook#D[A:notebook]")

page_html = url.read()
url.close()

soup = BeautifulSoup(page_html, "html.parser")

containers = soup.findAll("div", {
    "class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default"})

filename = "mercadolibre notebooks.csv"
f = open(filename, "w")

headers = ("Name,Price,Brand,\n")

f.write(headers)

for container in containers:
    product_name = container.findAll("h2", {"class": "ui-search-item__title"})
    name = product_name[0].text
    name = name.replace(",", ".")

    prodcut_price = container.findAll("span", {"class": "price-tag-fraction"})
    price = prodcut_price[0].text

    selling_brand = container.findAll(
        "p", {"class": "ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY"})
    try:
        brand = selling_brand[0].text
        if len(brand) < 0:
            brand = "No info"
    except:
        brand = "No info"
    print(name, "|", price, "|", brand)

    f.write(name + "," + price + "," + brand + "\n")

f.close()
