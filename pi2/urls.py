"""pi2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import include
from pyzza.views import Pizza_Viewset, Bebida_Viewset, TamanhoPizza_Viewset

from pi2 import settings
rotas_api = routers.DefaultRouter()
rotas_api.register('pizza',Pizza_Viewset,'SaborPizza')
rotas_api.register('bebida',Bebida_Viewset,"Bebida")
rotas_api.register('tamanho_pizza', TamanhoPizza_Viewset, 'TamanhoPizza')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas_api.urls)),#inclui as rotas da api, podendo criar mais rotas
    path('', include('pyzza.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
