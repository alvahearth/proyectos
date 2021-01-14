fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    linex = line.split()
    if not line.startswith("From:"):
        continue
    else:
        count = count + 1
        print(linex[1])
        

print("There were", count, "lines in the file with From as the first word")
