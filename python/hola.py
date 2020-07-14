palabra = "hola"
largo = len(palabra)
print(largo)
palabra_1 = palabra[::-1]
print(palabra_1)
count = 0

for char in palabra_1:
    count = count + 1
    print(count, char)
    
    
    