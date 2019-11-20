# Generated by Django 2.2.6 on 2019-11-11 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bebidas', '0001_initial'),
        ('pessoas', '0001_initial'),
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Forma de Pagamento',
                'verbose_name_plural': 'Formas de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='StatusPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Status do Pedido',
                'verbose_name_plural': 'Status de Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('troco_para', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoas.Cliente')),
                ('entregador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoas.Entregador')),
                ('forma_de_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pedidos.FormaDePagamento')),
                ('status_pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pedidos.StatusPedido')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('observacao', models.TextField(blank=True, default='', null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido')),
                ('sabor_borda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizzas.SaborBorda')),
                ('sabores', models.ManyToManyField(to='pizzas.SaborPizza')),
                ('tamanho_pizza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizzas.TamanhoPizza')),
            ],
        ),
        migrations.CreateModel(
            name='ItemBebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('bebida_tamanho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bebidas.BebidaTamanhoBebida')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido')),
            ],
        ),
    ]