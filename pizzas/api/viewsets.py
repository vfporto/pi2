from rest_framework import viewsets
from .serializers import SaborPizza_Serializer, TamanhoPizza_Serializer, SaborBorda_Serializer
from pizzas.models import SaborPizza, TamanhoPizza, SaborBorda


class TamanhoPizza_Viewset(viewsets.ModelViewSet):
    queryset = TamanhoPizza.objects.all()
    serializer_class = TamanhoPizza_Serializer


class SaborPizza_Viewset (viewsets.ModelViewSet):
    # TODO: corrigir queryset para fazer prefetch de TipoPizza
    queryset = SaborPizza.objects.filter(disponivel=True)
    # queryset = SaborPizza.objects.all()
    # queryset = queryset.prefetch_related()
    serializer_class = SaborPizza_Serializer

class SaborBorda_Viewset(viewsets.ModelViewSet):
    queryset = SaborBorda.objects.filter(disponivel=True)
    serializer_class = SaborBorda_Serializer