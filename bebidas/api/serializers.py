from rest_framework import serializers
from bebidas.models import TamanhoBebida, Bebida, BebidaTamanhoBebida

class TamanhoBebida_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TamanhoBebida
        fields = ('__all__')


class BebidaTamanhoBebida_Serializer(serializers.ModelSerializer):
    tamanho_bebida = TamanhoBebida_Serializer()

    class Meta:
        model = BebidaTamanhoBebida
        # fields = ('preco', 'bebida', 'tamanho_bebida')
        # fields = ('__all__')
        fields = ('id', 'preco', 'tamanho_bebida')

class Bebida_Serializer(serializers.ModelSerializer):
    # tamanhos = TamanhoBebida_Serializer(many=True, read_only=True)
    opcoes = BebidaTamanhoBebida_Serializer(many=True)

    class Meta:
        model = Bebida
        # fields = ('__all__')
        fields = ('id', 'nome', 'disponivel', 'tamanhos', 'opcoes')
        # fields = ('id', 'nome', 'disponivel', 'opcoes')

