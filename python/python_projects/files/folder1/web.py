import urllib
import urllib.request
import urllib.error
import re

fhand = urllib.request.urlopen("")
for line in fhand:
    print(line.decode().strip())
