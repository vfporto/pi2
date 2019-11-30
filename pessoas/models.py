from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=11, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)


class Entregador(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='endereco_entregador')


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Entregador'
        verbose_name_plural = 'Entregadores'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='endereco_cliente')

    # usuario = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

#
# class CustomUser(AbstractBaseUser):
#     pass