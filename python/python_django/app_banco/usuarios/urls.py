from os import name
from django.urls import path
from .views import (
    HomePage,
    RegisterUser,
    Profile,
    Transaction,
    Historial
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HomePage.as_view(), name="inicio"),
    path('registro/', RegisterUser.as_view(), name="registro"),

    path('perfil/', Profile.as_view(), name="perfil"),
    path('transferencia/', Transaction.as_view(), name="transferencia"),
    path('historial/<int:id>', Historial.as_view(), name="historial"),

    path('login/', LoginView.as_view(template_name="usuarios/login.html"),name="login"),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),
]