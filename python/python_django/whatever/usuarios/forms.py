from django import forms
from django.forms.fields import ImageField
from .models import CustomUser, PerfilModel ##
from .validators import check_email_domain
from django.contrib.auth.forms import UserCreationForm
from PIL import Image

class NewUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "****@gmail.com"}),
                            validators=[check_email_domain])
    rut = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "1234567890"}))
    
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'rut',
            'password1',
            'password2',
        ]
        
        
        
class UpdataUserImage(forms.ModelForm):
    imagen = forms.ImageField()
    
    class Meta:
        model = PerfilModel
        fields = [
            'imagen'
        ]
        
    