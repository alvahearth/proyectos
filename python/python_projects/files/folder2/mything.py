from io import open
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
ruta = os.path.join("/folder2", BASE_DIR)
print(ruta)

my_games = [
    {
        'genre':'action',
        'games': [
            'COD',
            'PUBG',
            'BATTLEFIELD',
        ]
    },
    {
        'genre': 'rpg',
        'games': [
            'FALLOUT',
            'WITCHER',
            'FINAL FANTASY'
        ]
    },
]

mi_archivo1 = ruta + "\\folder2\my_texto.txt"
mi_archivo2 = ruta + "\\folder2\my_texto.html"
mi_archivo3 = ruta + "\\folder2\my_texto.py"

print(mi_archivo1)

archivo1 = open(mi_archivo1, "a+")

for i in my_games:
    for j in i["games"]:
        archivo1.write(f"{j}\n")
        

# archivo2 = open(mi_archivo2, "a+")
# archivo3 = open(mi_archivo3, "a+")

# archivo2.write("<h1>hola</h1>")
# archivo3.write("print('hola mundo')")

archivo1.close()
# archivo2.close()
# archivo3.close()