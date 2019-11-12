from django.db import models
from bebidas.models import BebidaTamanhoBebida
from pizzas.models import TamanhoPizza, SaborBorda, SaborPizza
from pessoas.models import Entregador, Cliente
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models import F, Sum

# Pedido Models
class StatusPedido(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Status do Pedido'
        verbose_name_plural = 'Status de Pedidos'


class FormaDePagamento(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'


class Pedido(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True, null=True)
    troco_para = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    forma_de_pagamento = models.ForeignKey(FormaDePagamento, on_delete=models.PROTECT)
    status_pedido = models.ForeignKey(StatusPedido, on_delete=models.PROTECT)
    entregador = models.ForeignKey(Entregador, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def get_total(self):
        tot = 0
        for p in self.itens_pizza.all():
            print("------ item: " + p.__str__())
            tot += p.tamanho_pizza.preco
            tot += p.sabor_borda.valor_adicional

            subtot = 0
            for s in p.sabores.all():
                subtot += s.valor_adicional + s.tipo_pizza.valor_adicional
            subtot = subtot / p.sabores.count()
            tot += subtot

        print("%s %f" % ("tot: ", tot ))
        return tot

    def get_total2(self):
        print(self.itens_pizza.all().aggregate(teste=Sum('preco')))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        print("---------------salvando pedido------------------")
        # print(self.get_total())
        super().save(force_insert, force_update, using, update_fields)
        self.refresh_from_db()
        self.get_total()
        self.get_total2()




    def __str__(self):
        return self.data.strftime("%B %d, %Y, %I:%M %p") + " " + self.cliente.nome

# @receiver(m2m_changed, sender=Pedido.objects.itens_pizza.trough) # FIXME: essa m... só funciona muitos pra muitos
def update_pedido_total(sender, instance, **kwargs):
    pass


class ItemBebida(models.Model):
    quantidade = models.PositiveIntegerField(null=False, default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_bebida')
    # bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    bebida_tamanho = models.ForeignKey(BebidaTamanhoBebida, on_delete=models.PROTECT)


class ItemPizza(models.Model):
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    observacao = models.TextField(default='', blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pizza')
    tamanho_pizza = models.ForeignKey(TamanhoPizza, on_delete=models.PROTECT)
    sabor_borda = models.ForeignKey(SaborBorda, on_delete=models.PROTECT)
    # sabor_pizza = models.ForeignKey(SaborPizza, on_delete=models.PROTECT)
    sabores = models.ManyToManyField(SaborPizza)

    def __str__(self):  # Frufru pra sair no admin o nome do ItemPizza para o pedido
        titulo = self.tamanho_pizza.nome + " ("
        for sabor in self.sabores.all():
            titulo += "%s, " % sabor.nome
        titulo += ")"
        return titulo



    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     print("==== Item Pizza Save() ====")
    #     for s in self.sabores.all():
    #         print(s.nome)
    #     print("===========================")
    #     super().save(force_insert, force_update, using, update_fields)


