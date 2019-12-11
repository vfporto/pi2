from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from bebidas.models import BebidaTamanhoBebida
from pedidos.models import Pedido, FormaDePagamento, ItemPizza, ItemBebida
from pessoas.models import Cliente, Endereco
from pizzas.api.serializers import FormaDePagamento_Serializer
from pizzas.models import TamanhoPizza, SaborBorda, SaborPizza
from .serializers import PedidoSerializer, ItemPizzaSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class FormaDePagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaDePagamento.objects.all()
    serializer_class = FormaDePagamento_Serializer


# class EnvioPedido(APIView):
#
#     @classmethod
#     def get_extra_actions(cls):
#         return []
#
#     def get(self, request):
#         return Response({"message": "ok"})
#
#     def post(self, request):
#         pedido = request.data.get('pedido')
#         print(pedido)
#         return Response({"message": "ok"})


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication, SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def EnvioPedido(request):
    if request.method == 'POST':
        dados = request.data

        # cliente = Cliente.objects.filter(id=dados['cliente']).get()
        cliente = request.user.cliente
        forma_de_pagamento = FormaDePagamento.objects.filter(id=dados['forma_de_pagamento']['id']).get()
        troco_para = dados['troco_para']
        observacao = dados['observacao']

        print(cliente)
        print(forma_de_pagamento)
        print(troco_para)
        print(observacao)

        pedido = Pedido()

        pedido.cliente = cliente
        pedido.forma_de_pagamento = forma_de_pagamento
        pedido.troco_para = troco_para
        pedido.observacao = observacao

        pedido.save()
        print("Pedido: %d" % pedido.id)
        # Criacao de itens pizza
        itens_pizza = dados['itens_pizza']
        for ip in itens_pizza:
            tamanho = TamanhoPizza.objects.filter(id=ip['tamanho_pizza']['id']).get()
            sabor_borda = SaborBorda.objects.filter(id=ip['sabor_borda']['id']).get()
            quantidade = ip['quantidade']

            item = ItemPizza.objects.create(tamanho_pizza=tamanho,
                                            sabor_borda=sabor_borda, quantidade=quantidade, pedido=pedido)
            sabores = ip['sabores']
            for sabor in sabores:
                sabormodel = SaborPizza.objects.filter(id=sabor['id']).get()
                item.sabores.add(sabormodel)


        # Criacao dos itens-bebidas
        itens_bebida = dados['itens_bebida']
        print(itens_bebida)
        for ib in itens_bebida:
            opcao = BebidaTamanhoBebida.objects.filter(id=ib['id']).get()
            print(opcao)
            quantidade= ib['quantidade']
            item = ItemBebida.objects.create(quantidade=quantidade, pedido=pedido, bebida_tamanho=opcao)
            print(item)

        return Response({"message": "funcionou", "dados": request.data})
    return Response({"message": "ok"})


@api_view(['GET', 'POST'])
def CadastroCliente(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                dados = request.data
                dados_usuario = dados['usuario']
                dados_endereco = dados['endereco']

                usuario = User()
                usuario.email = dados_usuario['email']
                usuario.username = dados_usuario['username']
                usuario.set_password(dados_usuario['password'])
                usuario.save()
                usuario.groups.add(Group.objects.filter(name='Cliente').get())


                endereco = Endereco()
                endereco.logradouro = dados_endereco['logradouro']
                endereco.numero = dados_endereco['numero']
                endereco.complemento = dados_endereco['complemento']
                endereco.bairro = dados_endereco['bairro']
                endereco.cep = dados_endereco['cep']
                endereco.cidade = dados_endereco['cidade']
                endereco.uf = dados_endereco['uf']
                endereco.save()

                cliente = Cliente()
                cliente.nome = dados['nome']
                cliente.telefone = dados['telefone']
                cliente.endereco = endereco
                cliente.usuario = usuario
                cliente.save()
                return Response({"message": "Cliente criado com sucesso", "dados": request.data}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Nao foi possivel criar o cliente", "dados": request.data}, status=status.HTTP_403_FORBIDDEN)

    return Response({"message": "Rota cadastro_cliente está ONLINE"})