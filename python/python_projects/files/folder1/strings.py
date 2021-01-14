user_input = str(input("Ingresa un nombre: "))

name = user_input[::-1]

if name == user_input:
    print("palindrome")

print(name)

