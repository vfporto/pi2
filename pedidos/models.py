from django.db import models, transaction
from django.db.transaction import atomic
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from bebidas.models import BebidaTamanhoBebida
from pizzas.models import TamanhoPizza, SaborBorda, SaborPizza
from pessoas.models import Entregador, Cliente


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
    total = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    troco_para = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    forma_de_pagamento = models.ForeignKey(FormaDePagamento, on_delete=models.PROTECT, default=1)
    status_pedido = models.ForeignKey(StatusPedido, on_delete=models.PROTECT, default=1)
    entregador = models.ForeignKey(Entregador, on_delete=models.PROTECT, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    observacao = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.data.strftime("%B %d, %Y, %I:%M %p") + " " + self.cliente.nome

    def get_total(self):
        preco = 0
        for ip in self.itens_pizza.all():
            preco += ip.get_preco()
        for ib in self.itens_bebida.all():
            preco += ib.get_preco()
        return preco

    get_total.short_description = "Total"

    def calcula_total(self):
        Pedido.objects.filter(pk=self.id).update(total=self.get_total())

    def consumirIngredientes(self):
        #TODO: Utilizar funções de banco para consumirIngredientes
        itens_pizza = self.itens_pizza.all()
        for item in itens_pizza:
            num_sabores = item.sabores.count()
            if(num_sabores > 0):
                print("ItemPizza -> tamanho: %s (%d sabor(es)) -> Qtde: %s " % (item.tamanho_pizza.nome, num_sabores, item.quantidade))
                for sabor in item.sabores.all():
                    print("  %s %s" % ("SaborPizza: ", sabor.nome))
                    for ingrediente in sabor.ingredientes.all():
                        pivot = sabor.ingredientes_pivot.filter(ingrediente=ingrediente).get()
                        qt_consumo = ((pivot.quantidade * item.tamanho_pizza.multiplicador) * item.quantidade)/num_sabores
                        nova_quantidade = ingrediente.qt_estoque - qt_consumo
                        print("    %s :  %5.2f - %5.2f = %5.2f" % (
                            ingrediente.nome, ingrediente.qt_estoque, qt_consumo, nova_quantidade))
                        ingrediente.qt_estoque = nova_quantidade
                        ingrediente.save()
                borda = item.sabor_borda
                print("  %s %s" % ("SaborBorda: ", borda.nome))
                for ingrediente in borda.ingredientes.all():
                    pivot = borda.ingredientes_borda_pivot.filter(ingrediente=ingrediente).get()
                    qt_consumo = (pivot.quantidade * item.tamanho_pizza.multiplicador) * item.quantidade
                    nova_quantidade = ingrediente.qt_estoque - qt_consumo
                    print("    %s :  %5.2f - %5.2f = %5.2f" % (
                        ingrediente.nome, ingrediente.qt_estoque, qt_consumo, nova_quantidade))
                    ingrediente.qt_estoque = nova_quantidade
                    ingrediente.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        print("--------- PEDIDO PRE SAVE() ----------")
        # status_pedido == 2 -> "EM_PRODUCAO" --> se mudar isso vai dar problema...
        if(self.status_pedido.id==2): ## nome=="EM_PRODUCAO"):
            print("consumirIngredientes()")
            # self.total = self.get_total()
            # self.consumirIngredientes()
            try:
                with transaction.atomic():
                    self.consumirIngredientes()
            except:
                pass

        super().save(force_insert, force_update, using, update_fields)
        print("--------- PEDIDO POS SAVE() ----------")


class ItemBebida(models.Model):
    quantidade = models.PositiveIntegerField(null=False, default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_bebida')
    # bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    bebida_tamanho = models.ForeignKey(BebidaTamanhoBebida, on_delete=models.PROTECT)

    def get_preco(self):
        return self.bebida_tamanho.preco * self.quantidade

    get_preco.short_description = "Preço"


class ItemPizza(models.Model):
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    # observacao = models.TextField(default='', blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pizza')
    tamanho_pizza = models.ForeignKey(TamanhoPizza, on_delete=models.PROTECT)
    sabor_borda = models.ForeignKey(SaborBorda, on_delete=models.PROTECT)
    # sabor_pizza = models.ForeignKey(SaborPizza, on_delete=models.PROTECT)
    sabores = models.ManyToManyField(SaborPizza)

    # def __str__(self):  # Frufru pra sair no admin o nome do ItemPizza para o pedido
    #     titulo = self.tamanho_pizza.nome + " ("
    #     for sabor in self.sabores.all():
    #         titulo += "%s, " % sabor.nome
    #     titulo += ")"
    #     return titulo

    # TODO: criar viewset para devolver preco de um itempizza recebido do front
    def get_preco(self):
        preco = 0
        preco += self.tamanho_pizza.preco
        preco += self.sabor_borda.valor_adicional
        preco_sabores = 0
        for sabor in self.sabores.all():  # .filter(itempizza=self.pk):
            preco_sabores += sabor.tipo_pizza.valor_adicional
            preco_sabores += sabor.valor_adicional
        preco_sabores = preco_sabores / self.sabores.count()
        preco += preco_sabores
        preco *= self.quantidade
        # print(preco_sabores)
        return preco

    get_preco.short_description = "Preço"

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     print("----- Item Pizza POS SAVE() -----")
    #     self.pedido.total += self.tamanho_pizza.preco #nao funciona
    #     self.pedido.save()
    #
    #     print(self)
    #     super().save(force_insert, force_update, using, update_fields)
    #     print("----- Item Pizza POS SAVE() -----")

# @receiver(post_save, sender=ItemPizza)
# def update_pedido_total(sender, instance, **kwargs):
#     p = instance.pedido
#     instance.pedido.calcula_total()
#     # valor_total = instance.pedido.get_total()
#     # Pedido.objects.filter(pk=instance.pedido.id).update(total=valor_total)