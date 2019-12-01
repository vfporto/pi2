from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from pedidos.models import Pedido, StatusPedido, ItemPizza, ItemBebida
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
    lista = Entregador.objects.filter(pedido__status_pedido_id__gte=3, pedido__status_pedido_id__lte=4).distinct().prefetch_related(Prefetch('pedido', Pedido.objects.filter(status_pedido_id__gte=3, status_pedido_id__lte=4)))
    # lista = Entregador.objects.all()
    return render(request, 'site_interno/rel_entregadores.html', {'lista': lista})

@login_required(login_url='/admin/login')
def dashboard_pedidos(request):
    # TODO: corrigir a busca de pedidos do dashboard
    lista = Pedido.objects.filter(status_pedido_id__lt=4)
    entregadores = Entregador.objects.all()
    return render(request, 'site_interno/dashboard_pedidos.html', {'lista': lista, 'entregadores': entregadores})


@login_required(login_url='/admin/login')
def set_status_pedido(request, pedido_id, status_id):
    p = Pedido.objects.get(pk=pedido_id)
    p.status_pedido = StatusPedido.objects.get(pk=status_id)
    p.save()

    return HttpResponseRedirect('/interno/dashboard_pedidos/',request)


@login_required(login_url='/admin/login')
def set_status_pedido_em_entrega(request, pedido_id):
    entregador=request.POST['entregador']
    Pedido.objects.filter(pk=pedido_id).update(status_pedido=3, entregador=entregador)
    return HttpResponseRedirect('/interno/dashboard_pedidos/',request)

@login_required(login_url='/admin/login')
def rel_pizzas_produzidas(request):
    listapizzas = ItemPizza.objects.all()
    listabebidas = ItemBebida.objects.all()

    # entregador = Entregador.objects.all()
    return render(request, 'site_interno/rel_pizzas_produzidas.html', {'listapizzas': listapizzas, 'listabebidas': listabebidas})