import re

filehand = input("Enter name of the file: ")

try:
    fhand = open(filehand)
except:
    print("No such file exists")
    quit()
average = 0
for line in fhand:
    line = line.strip()
    x = re.findall("[0-9]+", line)
    for lines in x:
        numbers = int(lines)
        average = average + numbers

print(average)
