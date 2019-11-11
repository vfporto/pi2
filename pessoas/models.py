from django.contrib.auth.models import User
from django.db import models

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
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='endereco')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Entregador'
        verbose_name_plural = 'Entregadores'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    # para demais campos, integrar com classe User
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

