from django.db.models import Prefetch
from rest_framework import viewsets
from bebidas.models import Bebida, BebidaTamanhoBebida
from .serializers import Bebida_Serializer


class Bebida_Viewset(viewsets.ModelViewSet):
    # queryset = Bebida.objects.all()
    # queryset = Bebida.objects.filter(tamanhos__disponivel=True)
    queryset = Bebida.objects.filter(disponivel=True) \
        .prefetch_related(Prefetch('opcoes', queryset=BebidaTamanhoBebida.objects.filter(
            disponivel=True, tamanho_bebida__disponivel=True)))

    serializer_class = Bebida_Serializer
