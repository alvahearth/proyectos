fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    appendix = line.split()
    for w in appendix:
        value = w
        if value in lst:
            continue
        else:
            lst.append(value)

palabras = lst

palabras.sort()

print(palabras)
#primera1 = lst[0]
#primera2 = lst[1]
#primera3 = lst[2]
#primera4 = lst[3]
#
#palabrafinal = primera1 + primera2 + primera3 + primera4
#
#for w in palabrafinal:
#    print(w)
