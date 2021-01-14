# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        linex = line[19:]
        floating = float(linex)
        #print(floating)
        average = average + floating
            

final = average / count  


print("Average spam confidence:",final)

