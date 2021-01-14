file1 = open("romeo.txt")
fhand = file1.read()
lst = list()

pieces = fhand.split()

for w in pieces:
    value = w
    if value in lst:
        continue
    else:
        lst.append(value)

ordenado = lst
final = ordenado.sort()

print(ordenado)
