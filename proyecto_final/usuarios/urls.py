from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.usuarios, name="usuarios"),
    path("nuevo/", views.nuevo_usuario, name="nuevo_usuario"),
]
