import re

filex = input("Enter file name: ")
try:
    fh = open(filex)
except:
    print("No such file")
    quit()

average = 0
count = 0
for line in fh:
    line = line.strip()
    x = re.findall("X-DSPAM-Confidence:.*", line)
    for lines in x:
        y = re.findall(" .*", lines)
        for linex in y:
            number = float(linex)
            print(number)
            count = count + 1
            average = average + number

print("The average is:", average / count)
