from django.db import migrations

from pedidos.models import StatusPedido

# TODO: mudar essa migration para o app pedido
def populate(apps, schema_editor):
    lista = ['SOLICITADO', 'EM_PRODUCAO', 'EM_ENTREGA', 'CONCLUIDO', 'CANCELADO']
    for item in lista:
        status = StatusPedido(nome=item)
        status.save()



class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]

