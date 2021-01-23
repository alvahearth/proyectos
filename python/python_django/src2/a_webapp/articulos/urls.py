from django.urls import path
from .views import (
    RegistrarNuevoArticulo,
    ArticulosSistema
)

urlpatterns = [
    path('', RegistrarNuevoArticulo.as_view(), name="registro"),
    path('index/', ArticulosSistema.as_view(), name="lista")
]
