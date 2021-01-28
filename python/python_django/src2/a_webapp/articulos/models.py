from django.db import models
from django.utils import timezone

class Articulo(models.Model):
    titulo = models.CharField(max_length=50, unique=True, verbose_name="Titulo")
    contenido = models.TextField()
    fecha_publicado = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.titulo
