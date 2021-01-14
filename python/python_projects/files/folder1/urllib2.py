import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen(
    "https://py4e-data.dr-chuck.net/comments_843493.html"
).read()
soup = BeautifulSoup(fhand, "html.parser")

tags = soup("span")
average = 0
for tag in tags:
    x = tag.contents[0]
    num = int(x)
    average = average + num


print(average)
