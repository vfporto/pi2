from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pizzas.models import Ingrediente


@login_required(login_url='/admin/login')
def index(request):
    return render(request, 'index.html',{})

def rel_ingredientes(request):
    lista = Ingrediente.objects.all()
    return render(request, 'rel_ingredientes.html', {'lista': lista})


# # versao jefferson2
# from django.shortcuts import render
# 
# # Create your views here.
# def index(request):
#     return render(request, 'site_interno/index.html')
