fh = open("mbox-short.txt")

dictionary = dict()

for line in fh:
    line = line.strip()
    if line.startswith("From "):
        linex = line.split()
        linen = linex[2]
        for lines in linen:
            liney = linen
            # if liney not in dictionary:
            #dictionary[liney] = 1
            # else:
            #dictionary[liney] = dictionary[liney] + 1
            dictionary[liney] = dictionary.get(liney, 0) + 1

print(dictionary)
