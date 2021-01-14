largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        numero = int(num)
    except:
        print("Invalid Input")
        continue
    if numero > largest:
        largest = numero

    if smallest is None:
        smallest = numero
    elif numero < smallest:
        smallest = numero


print("Maximum is", largest)
print("Minimun is", smallest)
