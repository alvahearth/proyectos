import urllib.request 
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


url = urllib.request.urlopen("https://py4e-data.dr-chuck.net/comments_843495.xmls")

page = url.read()
url.close()

soup = BeautifulSoup(page,features="lxml")
average = 0
for lines in soup:
    lines = soup.commentinfo.comments
    line = lines.findAll("count")
    linex = line
    linec = linex[0:]
    for a in linec:
        b = int(a.text)
        average = average + b
        print(b)
        
print(average / 2)


