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
        fields = ('__all__')


class Bebida_Serializer(serializers.ModelSerializer):
    tamanhos = BebidaTamanhoBebida_Serializer(many=True, read_only=True)

    class Meta:
        model = Bebida
        # fields = ('__all__')
        fields = ('id', 'nome', 'tamanhos')

