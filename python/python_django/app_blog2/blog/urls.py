from os import name
from django.urls import path
from .views import (
    BorrarArticulo,
    ListaDeArticulos,
    ListaPorCategoria,
    CrearNuevoArticulo,
    EditarArticulo,
    ArticuloDetalle,
    ArticuloComentario,
    contacto_info,
    #ContactoInfo,
)

urlpatterns = [
    path('', ListaDeArticulos.as_view(), name="index"),
    path('nuevo/', CrearNuevoArticulo.as_view(), name="nuevo"),

    path('articulo_edit/<int:id>', EditarArticulo.as_view(), name="articulo_edit"),
    path('articulos/<int:id>', ArticuloDetalle.as_view(), name="detalle"),
    path('articulos/<int:id>/comentario', ArticuloComentario.as_view(), name="comentario"),
    path('categoria/<int:id>', ListaPorCategoria.as_view(), name="categorias"),
    path('borrar/<int:id>/borrar', BorrarArticulo.as_view(), name="borrar"),

    path('contacto/', contacto_info, name="contacto")
]