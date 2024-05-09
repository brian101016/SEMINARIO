from django.urls import path


from . import views


urlpatterns = [
    path("", views.index, name="bautizos"),
    path("crear/", views.crear_bautizo, name="crear_bautizo"),
    path("editar/<int:id>/", views.editar_bautizo, name="editar_bautizo"),
    path("eliminar/<int:id>/", views.eliminar_bautizo, name="eliminar_bautizo"),
]
