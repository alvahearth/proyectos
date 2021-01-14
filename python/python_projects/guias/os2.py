import os
lines = 200
n = 1

# set a variable to a specific path of your PC
x = os.environ.get("HOMEPATH")

#put a variable that points to a specific file and merge it with .join to path
file_path1 = os.path.join(x,"test.txt")
file_path2 = os.path.join(x,"test2.txt")


#wirte the files with a loop
with open(file_path1,"w") as wf:
    while lines > 1:
        if n % 2 == 0:
            wf.write("Numero par"+ " " + str(n) + "\n")
            n = n + 1
            lines = lines - 1
        else:
            wf.write(str(n) + "\n")
            n = n + 1
            lines = lines - 1