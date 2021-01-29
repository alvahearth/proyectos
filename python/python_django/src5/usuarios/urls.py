from django.urls import path
from .views import (
    UserRegistration
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', UserRegistration.as_view(), name="registro"),
    path('login/', LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name="logout")
]
