import math
import os
from random_word import RandomWords

r = RandomWords()

word = r.get_random_word().lower()
attemps = 10
count = 0

running = True

print(word[0:2])
while attemps > 0:
    user_input = input("\nIngresa una letra: ")

    if len(user_input) > 1:
        print("What are you doing?")
        continue
        
    if user_input in word[count]:
        print("Correcto")
        x = word[0:count + 1]
        print(x)
        count = count + 1
        
        if word == x:
            print("you win")
            break
    else:
        attemps = attemps - 1
        print(attemps)
        print("kweck")
        continue

if attemps == 0:
    print(word)    
    print("You lose")
        
else:
    print("You win")
    