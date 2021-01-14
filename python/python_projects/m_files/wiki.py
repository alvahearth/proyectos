import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import random

count = 4
passing = 0

while count > 0:
    if passing == 0:
        scrape = "https://es.wikipedia.org/wiki/Compsognathus_longipes"
        passing = passing + 1
        page = urllib.request.urlopen(scrape)

        url = page.read()
        page.close()

        soup = BeautifulSoup(url,"html.parser")

        text_container = soup.find("div",{"class":"mw-parser-output"})
    
        text = text_container.p.text
    
        print(text)

        all_links = soup.find(id="bodyContent").find_all("a")
        random.shuffle(all_links)

        for link in all_links:
            if link["href"].find("/wiki/") == 1:
                continue
        
            link_to_scrape = link
            break
    
        scrape = "https://en.wikipedia.org" + link_to_scrape['href']
        count = count - 1
    
    else:
        page = urllib.request.urlopen(scrape)

        url = page.read()
        page.close()

        soup = BeautifulSoup(url,"html.parser")

        text_container = soup.find("div",{"class":"mw-parser-output"})
    
        text = text_container.p.text
    
        print(text)

        all_links = soup.find(id="bodyContent").find_all("a")
        random.shuffle(all_links)

        for link in all_links:
            if link["href"].find("/wiki/") == 1:
                continue
        
            link_to_scrape = link
            break
    
        scrape = "https://en.wikipedia.org" + link_to_scrape['href']
        count = count - 1
