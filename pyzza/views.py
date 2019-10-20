from django.shortcuts import render
from django.http import HttpResponse
from pyzza.models import SaborPizza, TipoPizza, Bebida, BebidaTamanhoBebida, ItemBebida, TamanhoBebida
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

def contato(request):
 return render(request, 'pyzza/contato.html')


def cardapio(request):
 return render(request, 'pyzza/cardapio.html')


#classe de serializacao que transforma um model em JSON
class TipoPizza_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPizza
        fields = ('__all__')


class Pizza_Serializer(serializers.ModelSerializer):
    tipo_pizza = TipoPizza_Serializer()
    class Meta:
        model = SaborPizza
        # fields = ('__all__')
        fields = ('id', 'nome', 'descricao', 'valor_adicional', 'imagem','tipo_pizza')

# nao to conseguindo serializar igual a pizza
class BebidaTamanhoBebida_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BebidaTamanhoBebida
        fields = ('preco', 'bebida', 'tamanho_bebida')


class Bebida_Serializer(serializers.ModelSerializer):
    #tamanho_bebida = BebidaTamanhoBebida_Serializer()
    class Meta:
        model = Bebida
        fields = ('__all__')
        # fields = ('preco', 'bebida', 'tamanho_bebida')


class Pizza_Viewset (viewsets.ModelViewSet):
    # queryset = SaborPizza.objects.filter(disponivel=True)
    queryset = SaborPizza.objects.all()
    # queryset = queryset.prefetch_related()
    serializer_class = Pizza_Serializer


class Bebida_Viewset (viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = Bebida_Serializer




