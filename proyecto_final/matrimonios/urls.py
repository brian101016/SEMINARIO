from django.urls import path


from . import views


urlpatterns = [
    path("", views.index, name="matrimonios"),
    path("crear", views.crear_matrimonio, name="crear_matrimonio"),
    path("editar/<int:id>", views.editar_matrimonio, name="editar_matrimonio"),
    path("eliminar/<int:id>", views.eliminar_matrimonio, name="eliminar_matrimonio"),
]
