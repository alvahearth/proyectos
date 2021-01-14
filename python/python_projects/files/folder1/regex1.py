import re

fhand = input("Enter the name of the text: ")
try:
    filex = open(fhand)
except:
    print("File does not exist")
    quit()

finput = input("Enter a regular expression: ")
count = 0

if finput == "^Author":
    for line in filex:
        lineu = line.strip()
        x = re.findall("^Author", lineu)
        for lines in x:
            count = count + 1
            print(line)

if finput == "^X-":
    for line in filex:
        lineu = line.strip()
        x = re.findall("X-", lineu)
        for lines in x:
            count = count + 1
            print(line)
else:
    quit()
    print("Theres no lines")

print("There were", count, "Instances that matches the tag", lines)
# for lines in x:
# print(line)

