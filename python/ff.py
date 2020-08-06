import math
import os
import random
import re
import sys


number = input()
n = int(number)


if n >= 2 and n <= 5:
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0:
        print("Not Weird")

elif n >= 6 and n <= 20:
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0:
        print("Not Weird")

if n > 20:
    if n % 2 == 1:
        print("Weird")
        print(n)
    elif n % 2 == 0:
        print("Not Weird")
        print(n)
