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

from pizzas.api.viewsets import SaborPizza_Viewset, TamanhoPizza_Viewset, SaborBorda_Viewset
from bebidas.api.viewsets import Bebida_Viewset
from pedidos.api.viewsets import PedidoViewSet, FormaDePagamentoViewSet, EnvioPedido, CadastroCliente
from site_interno import views as site_interno_views

from pi2 import settings
from site_interno import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

rotas_api = routers.DefaultRouter()
rotas_api.register('sabor_pizza', SaborPizza_Viewset, 'SaborPizza')
rotas_api.register('sabor_borda', SaborBorda_Viewset, 'SaborBorda')
rotas_api.register('bebida',Bebida_Viewset,"Bebida")
rotas_api.register('tamanho_pizza', TamanhoPizza_Viewset, 'TamanhoPizza')
rotas_api.register('pedidos', PedidoViewSet, basename='Pedido')
rotas_api.register('forma_de_pagamento', FormaDePagamentoViewSet, 'FormaDePagamento')

# rotas_api.register('envio_pedido/', EnvioPedido, 'EnvioPedido')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas_api.urls)),#inclui as rotas da api, podendo criar mais rotas
    # path('interno/', include(site_interno_views.index)),
    path('interno/', include('site_interno.urls')),
    path('', include('pyzza.urls')),
    path('site_interno', views.index, name='index'),
    path('api/envio_pedido/', EnvioPedido),
    path('api/cadastro_cliente/', CadastroCliente),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header  = "Pyzzarella - Sistema de Gerenciamento"
admin.site.index_title = 'Painel de Administração'
admin.site.site_title = 'Seja bem vindo(a)'