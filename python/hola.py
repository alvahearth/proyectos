score = input("Enter Score: ")


try:
    nota = float(score)
    if nota > 1:
        print("out of range")
        quit()

except:
    quit()

if nota >= 0.9:
    print("A")
elif nota >= 0.8:
    print("B")
elif nota >= 0.7:
    print("C")
elif nota >= 0.6:
    print("D")
elif nota < 0.6:
    print("F")
