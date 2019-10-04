from django.shortcuts import render
from django.http import HttpResponse
from pyzza.models import SaborPizza
from rest_framework import serializers,viewsets
from rest_framework.filters import SearchFilter


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


#classe de serializacao que transforma um model em JSON
class Pizza_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SaborPizza
        fields = ('__all__')


class Pizza_Viewset (viewsets.ModelViewSet):
    queryset = SaborPizza.objects.all()
    serializer_class = Pizza_Serializer





