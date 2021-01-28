from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields import EmailField
from django.db.models.query_utils import select_related_descend
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, rut, nombre, apellido, user_n, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Ingresa tu correo")

        if not rut:
            raise ValueError("Ingresa tu rut")

        now = timezone.now()

        email = self.normalize_email(email)
        user = self.model( 
            email=email,
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            user_n=user_n,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email=None, rut=None, nombre=None,apellido=None, user_n=None, password=None, **extra_fields):
        return self._create_user(email, rut, nombre, apellido, user_n, password, False, False, **extra_fields)

    def create_superuser(self, email, rut, nombre, apellido, user_n, password, **extra_fields):
        
        user = self._create_user(email, rut, nombre, apellido , user_n, password, True, True, **extra_fields)
        user.save()
        return user



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Correo")
    rut = models.IntegerField(unique=True, default=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    user_n = models.CharField(max_length=100, unique=True, verbose_name="Nombre de usuario")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

# Create your models here.
