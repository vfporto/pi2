# Generated by Django 2.2.6 on 2019-11-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_auto_20191118_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='tamanhopizza',
            name='ordem',
            field=models.IntegerField(default=0),
        ),
    ]