import os
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

user_count = int(input("Enter count: "))
user_position = int(input("Enter position: "))
url = "https://py4e-data.dr-chuck.net/known_by_Raashi.html"

while user_count >= 0:
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = tags[user_position].get("href", None)
    user_count = user_count - 1
    print(url)

