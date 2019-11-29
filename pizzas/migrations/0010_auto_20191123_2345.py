# Generated by Django 2.2.5 on 2019-11-24 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0009_auto_20191122_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saborborda',
            options={'ordering': ['ordem', 'nome'], 'verbose_name': 'Sabor da Borda', 'verbose_name_plural': 'Sabores de Bordas'},
        ),
        migrations.AddField(
            model_name='saborborda',
            name='ordem',
            field=models.IntegerField(default=0),
        ),
    ]