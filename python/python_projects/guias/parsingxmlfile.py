import urllib.request 
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


url = urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_42.json")

page = url.read()
url.close()

soup = BeautifulSoup(page,"html.parser")

lines = soup.commentinfo.comments
line = lines.findAll("count")
average = 0
for b in line:
    print(b.text)
    average = average + int(b.text)
    
print(average)
