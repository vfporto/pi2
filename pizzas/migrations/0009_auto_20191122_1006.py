# Generated by Django 2.2.6 on 2019-11-22 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0008_auto_20191120_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saborbordaingrediente',
            options={'verbose_name': 'Ingrediente', 'verbose_name_plural': 'Ingredientes'},
        ),
        migrations.AlterModelOptions(
            name='saborpizzaingrediente',
            options={'verbose_name': 'Ingrediente', 'verbose_name_plural': 'Ingredientes'},
        ),
    ]
