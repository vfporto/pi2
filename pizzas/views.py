from django.shortcuts import render

from pizzas.models import SaborPizza


def mocha(request):
    lista = SaborPizza.objects.filter(disponivel=True)
    return render(request, 'pyzza/mocha.html', {'lista': lista})

