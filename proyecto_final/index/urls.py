"""
URL configuration for proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


from webapp import views


# Se generan las URLs según los módulos que estemos realizando.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("bautizos/", include("bautizos.urls")),
    path("comuniones/", include("comuniones.urls")),
    path("confirmaciones/", include("confirmaciones.urls")),
    path("matrimonios/", include("matrimonios.urls")),
    path("usuarios/", include("usuarios.urls")),
]
