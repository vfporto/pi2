from rest_framework import viewsets
from .serializers import Pizza_Serializer, TamanhoPizza_Serializer
from pizzas.models import SaborPizza, TamanhoPizza

class Pizza_Viewset (viewsets.ModelViewSet):
    queryset = SaborPizza.objects.filter(disponivel=True)
    # queryset = SaborPizza.objects.all()
    # queryset = queryset.prefetch_related()
    serializer_class = Pizza_Serializer

class TamanhoPizza_Viewset(viewsets.ModelViewSet):
    queryset = TamanhoPizza.objects.all()
    serializer_class = TamanhoPizza_Serializer
