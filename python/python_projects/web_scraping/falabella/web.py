from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://www.solotodo.cl/notebooks"

headers = {"User-Agent":"Mozilla/5.0"}

req = Request(url,headers=headers)

page = urlopen(req)

soup = BeautifulSoup(page,"html.parser")



containers = soup.findAll("div",{"class":"d-flex flex-column category-browse-result"})


for container in containers:

    product_name = container.h3.text

    product_price = container.findAll("div",{"class":"price flex-grow"})
    price = product_price[0].text

    product_specs = container.findAll("div",{"class":"description-container"})[0]

    print(product_name,price)
    for i in range(0,5):
        specs = product_specs.findAll("dd")[i]
        print(specs.text.strip())
        
    print("")