from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.fields import Field
from django.forms.forms import Form
from .models import Articulo, Comments
from django.contrib.auth.models import User
#from .validators import validar_rut
from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy as _

class NuevoArticulo(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = [
            'title',
            'content',
            'image',
            'category',
            'user'
        ]

class EditarArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = [
            'title',
            'content',
            'image'
        ]
    
class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    rut = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '12345678'}))
    email = forms.EmailField()
    telefono = forms.IntegerField()
    comentario = forms.CharField(widget=forms.Textarea(), required=False)

    fields = [
        'nombre',
        'rut',
        'email',
        'telefono',
        'comentario'
    ]

    def clean_rut(self): 
        rut = self.cleaned_data['rut']   
        numeroi = str(rut)
        if len(numeroi) < 9:
            raise ValidationError(_('Rut inválido'))

        lista_numeros = []

        contador = 2
        for i in numeroi[7::-1]:
            if contador > 7:
                contador = 2
            numero = contador * int(i)
            contador += 1
            lista_numeros.append(numero)

        sumatoria = 0
        for j in lista_numeros:
            sumatoria += j

        division = int(sumatoria / 11)
        multiplicado = division * 11
        final = 11 - (sumatoria - multiplicado)

        if final != int(numeroi[8]):
            raise ValidationError(_('Rut inválido'))
        
        return rut

class ComentarioForm(forms.ModelForm):
    

    class Meta:
        model = Comments
        fields = [
            'articulo',
            'name',
            'body'
        ]

class ConfirmarBorrar(forms.Form):
    fields = [
        'confirmar'
    ]
