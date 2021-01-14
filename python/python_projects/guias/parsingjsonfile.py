import urllib.request
import urllib.parse
import urllib.error
import json

url = urllib.request.urlopen("https://py4e-data.dr-chuck.net/comments_843496.json")

page = url.read()
url.close()

info = json.loads(page)


a = info.items()
b = info["comments"]

n = 0

for c in b:
    dictionary = c
    x = dictionary["count"]
    n = n +int(x)
    print(x)

print(n)




