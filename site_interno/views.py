from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
    lista = Entregador.objects.filter(pedido__status_pedido=3).distinct()
    # lista = Entregador.objects.all()
    return render(request, 'site_interno/rel_entregadores.html', {'lista': lista})