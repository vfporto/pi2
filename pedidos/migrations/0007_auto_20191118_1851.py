# Generated by Django 2.2.5 on 2019-11-18 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_auto_20191118_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='entregador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pessoas.Entregador'),
        ),
    ]
