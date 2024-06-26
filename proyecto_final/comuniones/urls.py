from django.urls import path


from . import views


# Se generan las URLs según la acción que estemos realizando.
urlpatterns = [
    path("", views.index, name="comuniones"),
    path("crear/", views.crear_comunion, name="crear_comunion"),
    path("editar/<int:id>/", views.editar_comunion, name="editar_comunion"),
    path("eliminar/<int:id>/", views.eliminar_comunion, name="eliminar_comunion"),
]
