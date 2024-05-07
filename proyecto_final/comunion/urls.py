from django.urls import path


from . import views


urlpatterns = [
    path("", views.comuniones, name="comuniones"),
    # path("datos_de_comunion", views.datos_de_comunion, name="datos_de_comunion"),
    path("crear/", views.crear_comunion, name="crear_comunion"),
    path("editar/<int:id>/", views.editar_comunion, name="editar_comunion"),
    path("eliminar/<int:id>/", views.eliminar_comunion, name="eliminar_comunion"),
]
