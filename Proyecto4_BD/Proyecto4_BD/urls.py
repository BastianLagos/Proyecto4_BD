"""Proyecto4_BD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from peliculas import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mostrarIndex),
    path('listado',views.mostrarListado),
    path('form_registrar',views.mostrarFormRegistrar),
    path('insertar',views.registrarPelicula),
    path('eliminar/<int:id>',views.eliminarPelicula),
    path('form_actualizar/<int:id>',views.mostrarFormActualizar),
    path('actualizar/<int:id>',views.actualizarPelicula),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)