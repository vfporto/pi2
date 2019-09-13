import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User


# Create your models here.

class Ingrediente(models.Model):
    nome = models.CharField(max_length=50)
    qt_estoque = models.IntegerField()
    qt_minima = models.IntegerField()
    qt_maxima = models.IntegerField()
    un_medida = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class TipoPizza(models.Model):
    nome = models.CharField(max_length=50)
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return self.nome


class SaborBorda(models.Model):
    nome = models.CharField(max_length=50)
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    #ingredientes = models.ManyToManyField(Ingrediente, related_name='ingredientes')

    def __str__(self):
        return self.nome


class SaborPizza(models.Model):
    nome = models.CharField(max_length=50)
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    tipo_pizza = models.ForeignKey(TipoPizza, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class SaborPizzaIngrediente(models.Model):
    sabor_pizza = models.ForeignKey(SaborPizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=7, default=0)


class SaborBordaIngrediente(models.Model):
    sabor_borda = models.ForeignKey(SaborBorda, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=7, default=0)


class TamanhoPizza(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(default='')
    max_sabores = models.IntegerField(default=1)
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    multiplicador = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return self.nome


# Bebidas
class TamanhoBebida(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Bebida(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class BebidaTamanhoBebida(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    tamanho_bebida = models.ForeignKey(TamanhoBebida, on_delete=models.CASCADE)


# Entregador e Cliente (provisorio)
class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)


class Entregador(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    # para demais campos, integrar com classe User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, null=True)

    def __str__(self):
        return self.nome



# Pedido

class StatusPedido(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class FormaDePagamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    data = models.DateTimeField(auto_now=True)
    total = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    troco_para = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    forma_de_pagamento = models.ForeignKey(FormaDePagamento, on_delete=models.PROTECT)
    status_pedido = models.ForeignKey(StatusPedido, on_delete=models.PROTECT)
    entregador = models.ForeignKey(Entregador, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.data + " " + self.cliente


class ItemBebida(models.Model):
    quantidade = models.PositiveIntegerField(null=False, default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    #bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    bebida_tamanho = models.ForeignKey(BebidaTamanhoBebida, on_delete=models.PROTECT)



class ItemPizza(models.Model):
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    observacao = models.TextField(default='')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tamanho_pizza = models.ForeignKey(TamanhoPizza, on_delete=models.PROTECT)
    sabor_borda = models.ForeignKey(SaborBorda, on_delete=models.PROTECT)
    #sabor_pizza = models.ForeignKey(SaborPizza, on_delete=models.PROTECT)
    sabores = models.ManyToManyField(SaborPizza)
