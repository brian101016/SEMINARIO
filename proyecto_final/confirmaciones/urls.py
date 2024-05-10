from django.urls import path


from . import views


# Se generan las URLs según la acción que estemos realizando.
urlpatterns = [
    path("", views.index, name="confirmaciones"),
    path("crear", views.crear_confirmacion, name="crear_confirmacion"),
    path("editar/<int:id>", views.editar_confirmacion, name="editar_confirmacion"),
    path("eliminar/<int:id>", views.eliminar_confirmacion, name="eliminar_confirmacion"),
]
