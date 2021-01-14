import re


fh = open("mbox-short.txt")

dictionary = dict()

for line in fh:
    line = line.strip()
    x = re.findall("X-DSPAM-Confidence:.*", line)
    for lines in x:
        dictionary[lines] = dictionary.get(lines, 0) + 1

for k, v in dictionary.items():
    print(k, v)
