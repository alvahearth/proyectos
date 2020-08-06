import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Opening the Web Page
url = urllib.request.urlopen(
    "https://www.pcfactory.cl/memorias-pc?categoria=112&papa=264&pagina=1"
)
# Storing the page into a variable
page_html = url.read()
url.close()

# Parsing the HTML code
soup = BeautifulSoup(page_html, "html.parser")

# Grabs all the containers
containers = soup.findAll("div", {"class": "wrap-caluga-matrix"})

# Pick one of the containers
containers[0]

# Store the picked container in a variable for prototyping
container = containers[0]

# Write the script to a csv file
filename = "products.csv"
f = open(filename, "w")

headers = "Brand, Price, Name\n"

f.write(headers)

# Find the specific tag that contains the item
for container in containers:
    brand_container = container.findAll("span", {"class": "marca"})
    brand = brand_container[0].text
    brand = brand.replace(" ", "")

    price_container = container.findAll("span", {"class": "txt-precio"})
    price = price_container[0].text
    price = price.replace(" ", "")

    name_container = container.findAll("span", {"class": "nombre"})
    name = name_container[0].text
    print(brand, "|", price, "|", name)

    f.write(brand + "," + price + "," + name + "\n")

f.close()

