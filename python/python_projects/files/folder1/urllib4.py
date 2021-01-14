import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen(
    "https://py4e-data.dr-chuck.net/known_by_Fikret.html"
).read()
soup = BeautifulSoup(fhand, "html.parser")

tags = soup("a")
count = 0
for tag in tags:
    print(tag)
