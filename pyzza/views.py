from django.shortcuts import render
from django.http import HttpResponse
from pyzza.models import SaborPizza


# Create your views here.
def home(request):
 return render(request, 'pyzza/home.html')


def login(request):
 return render(request, 'pyzza/login.html')


def pedido(request):
 return render(request, 'pyzza/pedido.html')

def mocha(request):
    lista = SaborPizza.objects.filter(disponivel=True)
    return render(request, 'pyzza/mocha.html', {'lista': lista})