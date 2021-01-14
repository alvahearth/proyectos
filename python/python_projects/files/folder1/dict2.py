fh = input("Ingresa el nombre del texto: ")
try:
    filex = open(fh)
except:
    print("invalid")
    quit()

dictionary = dict()

for line in filex:
    line = line.strip()
    if line.startswith("From:"):
        linex = line.split()
        linen = linex[1]
        linew = linen.split()
        for lines in linew:
            dictionary[lines] = dictionary.get(lines, 0) + 1

largest = None
lowest = None
largestname = None
lowestname = None

for a, b in dictionary.items():
    if largest is None or b > largest:
        largestname = a
        largest = b
    if lowest is None or b < lowest:
        lowestname = a
        lowest = b

print(largestname, largest)
print(lowestname, lowest)


#count = count + 1
# if largest < i:
#   largest = i
#count = count + 1
