import re

fhand = input("Ingrese el nombre del texto: ")

dictionary = dict()
try:
    fh = open(fhand)
except:
    print("Invalid")
    quit()

for line in fh:
    lineu = line.lower()
    # lineu = lineu.strip()
    # lineu = lineu.split()
    x = re.findall("[a-z]+", lineu)
    for liney in x:
        linew = liney.split()
        for linew in liney:
            # if linew.startswith("("):
            #    continue
            # elif linew.startswith("1"):
            #    continue
            # elif linew.startswith("8"):
            #    continue
            # else:
            lineb = linew[0]
            dictionary[lineb] = dictionary.get(lineb, 0) + 1


for k, v in sorted(dictionary.items()):
    print(k, v)
