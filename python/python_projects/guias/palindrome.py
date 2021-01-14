def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    palabra_inversa = palabra[::-1]
    if palabra == palabra_inversa:
        return "es un palíndromo"
    else:
        return "no es un palindromo"


if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    es_palindromo = palindromo(palabra)
    print("la palabra "+ palabra + " " + es_palindromo)