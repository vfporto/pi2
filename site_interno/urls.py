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
from django.contrib import admin
from django.urls import path

from site_interno import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rel_ingredientes/', views.rel_ingredientes, name='rel_ingredientes'),
    path('dashboard_pedidos/', views.dashboard_pedidos, name='dashboard_pedidos'),
    path('rel_entregadores/', views.rel_entregadores, name='rel_entregadores'),
    path('rel_pizzas_produzidas/', views.rel_pizzas_produzidas, name='rel_pizzas_produzidas'),
    path('set_status_pedido/<pedido_id>/<status_id>', views.set_status_pedido, name='set_status_pedido'),
    path('set_status_pedido_em_entrega/<pedido_id>/', views.set_status_pedido_em_entrega, name='set_status_pedido_em_entrega'),

]
