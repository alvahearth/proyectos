from django import forms
from .models import Articulo

class NuevoArticulo(forms.ModelForm):
    
    
    class Meta:
        model = Articulo
        fields = [
            'titulo',
            'contenido',
        ]