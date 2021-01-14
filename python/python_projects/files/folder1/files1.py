filehand = input("Ingresa el nombre del texto: ")
if filehand == "na na boo boo":
    print("What the fuck dude")
    quit()

newfile = open(filehand)

filex = newfile
count = 0
average = 0


for line in filex:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        linex = line.split(" ")
        floating = float(linex[1])
        average = average + floating

print(average / count)
