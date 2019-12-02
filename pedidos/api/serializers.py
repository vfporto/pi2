from rest_framework import serializers

from bebidas.api.serializers import BebidaTamanhoBebida_Serializer
from pedidos.models import Pedido, ItemPizza, StatusPedido, FormaDePagamento, ItemBebida

from pizzas.api.serializers import SaborBorda_Serializer, SaborPizza_Serializer, TamanhoPizza_Serializer

class StatusPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPedido
        fields = ('__all__')

class FormaDePagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaDePagamento
        fields = ('__all__')

class ItemBebidaSerializer(serializers.ModelSerializer):
    # bebida_tamanho = BebidaTamanhoBebida_Serializer()
    class Meta:
        model = ItemBebida
        fields = ('__all__')

class ItemPizzaSerializer(serializers.ModelSerializer):
    # sabores = SaborPizza_Serializer(many=True)
    # sabor_borda = Sabor_BordaSerializer()
    # tamanho_pizza = TamanhoPizza_Serializer()
    class Meta:
        model = ItemPizza
        fields = ('__all__')

class PedidoSerializer(serializers.ModelSerializer):
    itens_pizza = ItemPizzaSerializer(many=True)
    itens_bebida = ItemBebidaSerializer(many=True)
    # forma_de_pagamento = FormaDePagamentoSerializer()
    # status_pedido = StatusPedidoSerializer()

    class Meta:
        model = Pedido
        fields = ('__all__')
