from rest_framework import viewsets
from pedidos.models import Pedido, FormaDePagamento
from pizzas.api.serializers import FormaDePagamento_Serializer
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class FormaDePagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaDePagamento.objects.all()
    serializer_class = FormaDePagamento_Serializer