from django.urls import path
from . import views
from matrimonios import views as views_matrimonio
urlpatterns=[
  path('', views.index),
  path('matrimonios/', views_matrimonio.mostrarMatrimonios, name='index'),
  path('matrimonios/create', views_matrimonio.nuevoMatrimonio, name='create'),
  path('matrimonios/delete/<int:id>', views_matrimonio.eliminarMatrimonio, name='delete'),
  path('matrimonios/update/<int:id>', views_matrimonio.editarMatrimonio, name='update')
]
