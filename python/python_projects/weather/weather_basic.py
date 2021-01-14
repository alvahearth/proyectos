from urllib.request import Request,urlopen
import requests
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/weather/"

headings = {"User-Agent":"Mozilla/5.0"}

req = Request(url,headers=headings)

page = urlopen(req)

soup = BeautifulSoup(page,"html.parser")

containers = soup.findAll("div",{"class":"my-city__items"})

container = containers[0]

for i in range(0,4):
    cities = ["Santiago","New york","London","Tokyo"]
    chile_weather = container.findAll("span",{"class":"my-city__temp"})[i].text.rstrip()
    print(cities[i],chile_weather)