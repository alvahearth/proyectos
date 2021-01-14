fhand = input("Enter file name: ")

dictionary = dict()

try:
    fh = open(fhand)
except:
    print("invalid")
    quit()

for line in fh:
    line = line.strip()
    if line.startswith("From "):
        linex = line.split()
        liney = linex[5]
        linew = liney.split(":")
        linez = linew[0]
        linea = linez.split()
        for lines in linea:
            dictionary[lines] = dictionary.get(lines, 0) + 1


for key, value in sorted(dictionary.items()):
    print(key, value)
