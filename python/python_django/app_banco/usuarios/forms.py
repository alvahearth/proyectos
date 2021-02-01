from django import forms
from django.core import validators
from django.forms import fields
from .models import CustomUser, Profile, Dinero, MoverDinero
from django.contrib.auth.forms import UserCreationForm
from .validators import validate_something


class NewUserForm(UserCreationForm):
    rut = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "123456789"}),validators=[validate_something])
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "****@gmail.com"}))

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'rut',
            'password1',
            'password2',       
        ]


class UpdatePerfil(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['imagen']


class MakeTransfer(forms.ModelForm):

    class Meta:
        model = MoverDinero
        fields = ['dinero']