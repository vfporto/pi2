from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.filters import SearchFilter


# Create your views here.
def home(request):
    return render(request, 'pyzza/home.html')


def login(request):
    return render(request, 'pyzza/login.html')


def pedido(request):
    return render(request, 'pyzza/pedido.html')


def contato(request):
    return render(request, 'pyzza/contato.html')


def cardapio(request):
    return render(request, 'pyzza/cardapio.html')

