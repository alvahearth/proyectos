import re

filehand = open("mbox-short.txt")
fh = filehand

count = 0
average = 0
for lines in fh:
    lines = lines.strip()
    x = re.findall("New Revision:.*", lines)
    for line in x:
        lineu = line.split()
        lineb = lineu[2]
        linec = int(lineb)
        count = count + 1
        average = average + linec

print(int(average / count))

