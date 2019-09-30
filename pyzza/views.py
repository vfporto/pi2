from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
 return render(request, 'pyzza/home.html')


def login(request):
 return render(request, 'pyzza/login.html')


def pedido(request):
 return render(request, 'pyzza/pedido.html')