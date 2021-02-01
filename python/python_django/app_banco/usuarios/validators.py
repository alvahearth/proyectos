from django.core.exceptions import ValidationError

def validate_something(value):
                
    numeroi = str(value)

    inicial = []

    contador = 2
    for i in numeroi[7::-1]:
        if contador > 7:
            contador = 2
        numero = int(i) * contador
        contador += 1
        inicial.append(numero)

    sumatoria = 0
    for j in inicial:
            sumatoria += j

    division = int(sumatoria / 11)
    multiplicado = division * 11
    final = 11 - (sumatoria - multiplicado)

    if final != int(numeroi[8]):
        raise ValidationError("El rut no es correcto")
    return value