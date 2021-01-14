from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import csv

url = urllib.request.urlopen("https://www.pcfactory.cl/tarjetas-graficas-nvidia?categoria=378&papa=334")

page = url.read()
url.close()

soup = BeautifulSoup(page,"html.parser")

containers = soup.findAll("div",{"class":"wrap-caluga-matrix"})

csv_file = open("graphic_cards.csv","w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name","Price","Brand"])


for container in containers:    

    product_name = container.findAll("span",{"class":"nombre"})
    name = product_name[0].text 

    product_price = container.findAll("span",{"class":"txt-precio"})
    price = product_price[0].text
    price = price.replace(" ", "")
    price = price.replace("$", "")

    product_brand = container.findAll("span",{"class":"marca"})
    brand = product_brand[0].text
    brand = brand.replace(" ", "")
    brand = brand.replace("®", "")
    
    print(name,price,brand)
    
    csv_writer.writerow([name,price,brand])
    
csv_file.close()
