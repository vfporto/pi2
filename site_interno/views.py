from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render

from pedidos.models import Pedido
from pessoas.models import Entregador
from pizzas.models import Ingrediente


@login_required(login_url='/admin/login')
def index(request):
    return render(request, 'site_interno/index.html', {})


@login_required(login_url='/admin/login')
def rel_ingredientes(request):
    lista = Ingrediente.objects.all()
    return render(request, 'site_interno/rel_ingredientes.html', {'lista': lista})

@login_required(login_url='/admin/login')
def rel_entregadores(request):
    lista = Entregador.objects.filter(pedido__status_pedido=3).distinct().prefetch_related(Prefetch('pedido', Pedido.objects.filter(status_pedido=3)))
    # lista = Entregador.objects.all()
    return render(request, 'site_interno/rel_entregadores.html', {'lista': lista})

@login_required(login_url='/admin/login')
def dashboard_pedidos(request):
    # TODO: corrigir a busca de pedidos do dashboard
    lista = Pedido.objects.filter(status_pedido_id__lt=3)
    return render(request, 'site_interno/dashboard_pedidos.html', {'lista': lista})

