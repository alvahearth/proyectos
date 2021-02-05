from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager
from PIL import Image
from django.db.models.query_utils import select_related_descend
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, rut, password, **extra_fields):
        if not email:
            raise ValueError

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            rut=rut,
            **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, rut, password, **extra_fields):
        return self._create_user(email, rut, password, **extra_fields)

    def create_superuser(self, email, rut, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        user = self._create_user(email, rut, password, **extra_fields)
        user.save()

        return user

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Correo")
    rut = models.IntegerField(unique=True, verbose_name="Rut")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Última conexión")
    last_login = models.DateTimeField(default=timezone.now, verbose_name="Última conexión")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'rut'
    ]

    objects = CustomUserManager()

    def __str__(self):
        return f"Email: {self.email}"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    imagen = models.ImageField(default="default.jpg", upload_to="imagenes_perfil")

    def __str__(self):
        return f"Email: {self.user.email}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.imagen.path)

        if img.width > 300 or img.width > 300:
            size = (300,300)
            img.thumbnail(size)
            img.save(self.imagen.path)


class Dinero(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dinero = models.IntegerField(default=500)

    def __str__(self):
        return f"Dinero pertenece a {self.user}"

class MoverDinero(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dinero = models.IntegerField(default=0)
    fecha_de_movimiento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"usario {self.user}"
# from django import forms
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager
# from PIL import Image


# class CustomUserManager(BaseUserManager):

#     def create_user(self, email,rut , password, **extra_fields):

#         if not email:
#             raise ValueError(("Ingresa el rut"))

#         email = self.normalize_email(email)
#         #rut = self.model(IntegerField())
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()

#         return user

#     def create_superuser(self, email, password, **extra_fields):

#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     rut = models.IntegerField(unique=True,default=0)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

# class Perfil(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     imagen = models.ImageField(default="default.jpg", upload_to="imagenes_perfil/")

#     def __str__(self):
#         return f"Perfil {self.user}"

#     def save(self):
#         super().save()

#         img = Image.open(self.imagen.path)

#         if img.height > 300 or img.width > 300:
#             output = (300, 300)
#             img.thumbnail(output)
#             img.save(self.imagen.path)



