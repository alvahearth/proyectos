def split_str(s):
    return [ch for ch in s]


fhand = input("Ingresa el nombre del texto: ")

dictionary = dict()

try:
    fh = open(fhand)
except:
    print("Invalido")
    quit()

for w in fh:
    w = w.strip()
    linex = split_str(w)
    for lines in linex:
        if lines.startswith(" "):
            continue
        if lines.startswith("!"):
            continue
        if lines.startswith(","):
            continue
        if lines.startswith("."):
            continue
        if lines.startswith("?"):
            continue
        else:
            linec = lines.lower()
            dictionary[linec] = dictionary.get(linec, 0) + 1
largest = None
largestName = None
smallest = None
smallestName = None
for k, v in sorted(dictionary.items()):
    print(k, v)
    if largest is None or v > largest:
        largestName = k
        largest = v
    if smallest is None or v < smallest:
        smallestName = k
        smallest = v

print("--------------------")
print(largestName, largest)
print(smallestName, smallest)
# for lines in w:
#    lines.split()
#   linex = lines.split()
#  print(linex)
# linec = linex[:10]
# for linen in linex:
# linen = linex.split()
# print(linen)
