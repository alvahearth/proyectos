from django.contrib.auth.models import AnonymousUser
from django.urls import path
from .views import (
    UserRegistration,
    ListUsers,
    Profile,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', UserRegistration.as_view(), name="registro"),
    path('lista/', ListUsers.as_view(), name="lista"),
    path('login/', LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),
    path('perfil/', Profile.as_view(), name="perfil")
]
