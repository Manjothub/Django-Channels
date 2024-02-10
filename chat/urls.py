from django.urls import path

from .views import *

urlpatterns = [
    path("chat", INDEX, name="index"),
    path("login", LOGIN, name="login"),
    path("logout", LOGOUT, name="logout"),
]