import os
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://py4e-data.dr-chuck.net/known_by_Fikret.html")

html = url.read()
url.close()

soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
count = 0
for tag in tags:
    count = count + 1
    print("URL:", tag.get("href", None))
