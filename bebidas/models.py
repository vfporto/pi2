from django.db import models


# Bebidas
class TamanhoBebida(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tamanho da Bebida'
        verbose_name_plural = 'Tamanhos de Bebidas'


class Bebida(models.Model):
    nome = models.CharField(max_length=50)
    tamanhos = models.ManyToManyField(TamanhoBebida, through='BebidaTamanhoBebida', related_name='bebidas')

    def __str__(self):
        return self.nome


class BebidaTamanhoBebida(models.Model):
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)#, related_name='tamanhos')
    tamanho_bebida = models.ForeignKey(TamanhoBebida, on_delete=models.CASCADE)#, related_name='bebidas')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.bebida.nome, self.tamanho_bebida.nome)

