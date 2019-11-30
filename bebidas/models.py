from django.db import models


# Bebidas
class TamanhoBebida(models.Model):
    nome = models.CharField(max_length=50)
    ordem = models.IntegerField(default=0)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tamanho da Bebida'
        verbose_name_plural = 'Tamanhos de Bebidas'


class Bebida(models.Model):
    nome = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)
    tamanhos = models.ManyToManyField(TamanhoBebida, through='BebidaTamanhoBebida', related_name='bebidas')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class BebidaTamanhoBebida(models.Model):
    tamanho_bebida = models.ForeignKey(TamanhoBebida, on_delete=models.CASCADE)#, related_name='bebidas')
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE, related_name='opcoes')#, related_name='tamanhos')
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    disponivel = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Opção de Bebida'
        verbose_name_plural = 'Opções de Bebida'
    def __str__(self):
        return '%s - %s' % (self.bebida.nome, self.tamanho_bebida.nome)

