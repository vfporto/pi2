from django.shortcuts import render

# Create your views here.
from pyzza.models import SaborPizza


def mocha(request):
    lista = SaborPizza.objects.filter(disponivel=True)
    return render(request, 'pyzza/mocha.html', {'lista': lista})