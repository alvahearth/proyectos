from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields import EmailField
from django.db.models.query_utils import select_related_descend

class CustomUserManager(BaseUserManager):

    def create_user(self, email, rut, nombre, apellido, user_n, password, **extra_fields):
        if not email:
            raise ValueError("Ingresa tu correo")

        if not rut:
            raise ValueError("Ingresa tu rut")

        email = self.normalize_email(email)
        user = self.model( 
            email=email, **extra_fields,
            rut=rut, **extra_fields
        )
        user.set_password(password)
        user.save()

    def create_superuser(self, email, rut, nombre, apellido, user_n, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, rut, nombre, apellido , user_n, password, **extra_fields)



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Correo")
    rut = models.IntegerField(unique=True, default=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    user_n = models.CharField(max_length=100, unique=True, verbose_name="Nombre de usuario")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "rut",
        "nombre",
        "apellido",
        "user_n",
    ]

    objects = CustomUserManager()

# Create your models here.
