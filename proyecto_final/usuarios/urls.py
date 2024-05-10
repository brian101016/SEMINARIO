from django.contrib import admin
from django.urls import path, include


from . import views


# Se generan las URLs según la acción que estemos realizando.
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.index, name="usuarios"),
    path("crear/", views.crear_usuario, name="crear_usuario"),
    path("editar/<int:id>/", views.editar_usuario, name="editar_usuario"),
    path("eliminar/<int:id>/", views.eliminar_usuario, name="eliminar_usuario"),
]
