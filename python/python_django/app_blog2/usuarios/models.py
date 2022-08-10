import os
from os.path import join
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from app_blog2.settings.base import BASE_DIR

class PerfilDelUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default_profile.jpg", upload_to="profile_images", verbose_name="Imagen")
    about_me = models.CharField(max_length=40, verbose_name="Sobre mí", blank=True)
   
    class Meta:
        verbose_name = "Perfil del usuario"
        verbose_name_plural = "Perfiles de los usuarios"

    def __str__(self):
        return f" Perfil de:{self.user}"
