import re
import urllib.request
import urllib.parse
import urllib.error

# from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://motherfuckingwebsite.com/")
# soup = BeautifulSoup(html, "html.parser")

# tags = soup("a")
for lines in html:
    print(lines.strip())
