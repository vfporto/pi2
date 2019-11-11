from rest_framework import serializers
from pizzas.models import SaborPizza, Ingrediente, SaborPizzaIngrediente, TipoPizza, TamanhoPizza


class Ingrediente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('__all__')

class SaborPizzaIngrediente_Serializer(serializers.ModelSerializer):
    ingrediente = Ingrediente_Serializer()
    class Meta:
        model = SaborPizzaIngrediente
        fields = ('__all__')

#classe de serializacao que transforma um model em JSON
class TipoPizza_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPizza
        fields = ('__all__')


class Pizza_Serializer(serializers.ModelSerializer):
    tipo_pizza = TipoPizza_Serializer()
    ingredientes = SaborPizzaIngrediente_Serializer(many=True, read_only=True)
    class Meta:
        model = SaborPizza
        # fields = ('__all__')
        fields = ('id', 'nome', 'descricao', 'valor_adicional', 'imagem','tipo_pizza', 'ingredientes')



class TamanhoPizza_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TamanhoPizza
        fields = ('__all__')

