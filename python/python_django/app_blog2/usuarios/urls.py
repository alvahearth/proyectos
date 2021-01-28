from django.urls import path
from .views import (
    RegisterNewUser,
    ListViewUsers
)

urlpatterns = [
    path('', RegisterNewUser.as_view(), name="registro"),
    path('lista/', ListViewUsers.as_view(), name="lista")
]