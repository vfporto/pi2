from rest_framework import viewsets
from bebidas.models import Bebida
from .serializers import Bebida_Serializer

class Bebida_Viewset(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = Bebida_Serializer
