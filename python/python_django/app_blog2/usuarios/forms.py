from io import RawIOBase
from django.db.models.query import prefetch_related_objects
from django.forms.widgets import HiddenInput
from django.http.request import UnreadablePostError
from django.shortcuts import redirect, render
from .models import CustomUser
from django import forms

class NewUserForm(forms.ModelForm):
    rut = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "1234567890"}))
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    passcheck = forms.CharField(widget=forms.PasswordInput(), label="Verifica tu contraseña")

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'rut',
            'nombre',
            'apellido',
            'user_n',
            'password',
            'passcheck'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        passcheck = cleaned_data.get('passcheck')

        if password != passcheck:
            raise forms.ValidationError('Los campos no coinciden')

        return cleaned_data