line = '*'
space = " " * 10
max_length = 5

fila = ""
mas_estrellas = 1
while len(line) <= max_length:
    print(space + line + fila)
    if len(line) > 0:
        fila = "*" * mas_estrellas
        mas_estrellas = mas_estrellas + 1 
    space = space[:-1] 
    line = line + "*"

count = 5
menos_estrellas = mas_estrellas - 1
while len(line) > 0:
    print(" "*count+ line + fila)
    if len(line) > 0:
        menos_estrellas = menos_estrellas - 1
        fila = "*" * menos_estrellas
    line = line[:-1]
    count += 1