from django.forms import ValidationError

def check_email_domain(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("El dominio debe terminar con @gmail.com")
    
    return value