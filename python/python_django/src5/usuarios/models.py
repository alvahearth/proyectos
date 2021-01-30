from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.utils.translation import ugettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):
    
    def _create_user(self, email, rut,password, **extra_fields):
        if not email:
            raise ValueError('Ingresa un correo valido')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            rut=rut,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_user(self, email, rut, password, *extra_fields):
        return self._create_user(email, rut, password, **extra_fields)
    
    def create_superuser(self, email, rut, password, **extra_fields):
        
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_staff', True)
        
        user = self._create_user(email, rut, password, **extra_fields)
        user.save()
        
        return user
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Correo'), unique=True)
    rut = models.IntegerField(_('Rut'), unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'rut'
    ]
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"Email {self.email}"

class PerfilModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    imagen = models.ImageField(default="default.png", upload_to="profile_pics/")

    def __str__(self):
        return f"Usuario: {self.user}"