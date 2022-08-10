from django.forms import fields
from usuarios.models import PerfilDelUsuario
from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterNewUser(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class ActualizarDatos(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

class ActualizarFoto(forms.ModelForm):

    class Meta:
        model = PerfilDelUsuario
        fields = [
            'image'
        ]

class ActualizardSobreMi(forms.ModelForm):
    about_me = forms.CharField(label="Sobre mí",widget=forms.TextInput(attrs={'placeholder': "Cuentame sobre tí en 40 letras o menos"}))

    class Meta:
        model = PerfilDelUsuario
        fields = [
            'about_me'
        ]