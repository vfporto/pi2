from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pizzas.models import Ingrediente


@login_required(login_url='/admin/login')
def index(request):
    return render(request, 'site_interno/index.html', {})


@login_required(login_url='/admin/login')
def rel_ingredientes(request):
    lista = Ingrediente.objects.all()
    return render(request, 'site_interno/rel_ingredientes.html', {'lista': lista})
