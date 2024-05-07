from django.urls import path
from . import views
from confirmacion import views as views_confirmacion
urlpatterns=[
  path('', views.index),
  path('confirmacion/', views_confirmacion.index, name='index'),
  path('confirmacion/create', views_confirmacion.create, name='create'),
  path('confirmacion/update/<int:confirmacion_id>', views_confirmacion.update, name='update'),
  path('confirmacion/delete/<int:confirmacion_id>', views_confirmacion.delete, name='delete')
]
