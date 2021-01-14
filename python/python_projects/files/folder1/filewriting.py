import os 

x = os.environ.get("HOMEPATH")
file_path2 = os.path.join(x,"text2.txt")

with open(file_path2,"r") as rf:
    with open("test2.txt","w") as wf:
        for lines in rf:
            wf.write(lines)