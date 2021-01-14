import random
import string

password = []
letters = string.ascii_letters


for i in range(1,15):
    if i % 2 == 0:    
        i = random.choice(letters)
        password.append(i)
    else:
        i = random.randint(1,9)
        password.append(i)

x = random.sample(password,k=14)

for i in x:
    print(i,end="")