from django.urls import path
from .views import (
    #NuevoUsuario,
    nuevo_usuario,
    PerfilUsuario,
    ActualizarPerfil
)

from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [

    path('perfil', PerfilUsuario.as_view(), name="perfil"),
    path('actualizar_perfil/', ActualizarPerfil.as_view(), name="act_perfil"),

    #path('nuevo/', NuevoUsuario.as_view(), name="registro"),
    path('nuevo/', nuevo_usuario, name="registro"),

    path('login/', LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),

    path('reset/', PasswordResetView.as_view(template_name="usuarios/password_reset.html"), name="password_reset"),

    path('reset/done/', PasswordResetDoneView.as_view(template_name="usuarios/password_reset_done.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="usuarios/password_reset_confirm.html"), name="password_reset_confirm"),

    path('reset_complete/', PasswordResetCompleteView.as_view(template_name="usuarios/password_reset_complete.html"), name="password_reset_complete")
]
