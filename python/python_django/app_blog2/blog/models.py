from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils import tree
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el ")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.title

class Articulo(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default="default.jpg", upload_to="imageArticles/", verbose_name="Imagen")
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category ,verbose_name="Categoría", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el ")

    class Meta:
        ordering = ['created_at']
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return f"Nombre: {self.title}"


class Comments(models.Model):
    articulo = models.ForeignKey(Articulo, verbose_name="Árticulo", related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=100, verbose_name="Comentario")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.articulo.title} - {self.name}"


