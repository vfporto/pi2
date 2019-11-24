from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin

from .models import Entregador, Cliente


# class PaisAdmin(admin.ModelAdmin): # EXEMPLO ADMIN
#     search_fields = ['nome']
#     inlines = [EstadoAdminInline]
#     list_display = ['id','nome']
#     list_editable = ['nome']
#     ordering = ['nome']

class EntregadorAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    search_fields = ['nome']
    inline_reverse = [
        ('endereco', {'fields': ['logradouro', 'numero', 'complemento', 'bairro', 'cidade','cep', 'uf']}),
    ]


class ClienteAdmin(ReverseModelAdmin):
    model = Cliente
    inline_type = 'stacked'
    search_fields = ['id', 'nome', 'telefone']
    list_display = ['id', 'nome', 'telefone']
    list_display_links = ['id', 'nome', 'telefone']
    inline_reverse = [
        ('endereco', {'fields': ['id', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'cep', 'uf']}),
    ]
    # inline_reverse = ['endereco']


admin.site.register(Entregador, EntregadorAdmin)
admin.site.register(Cliente, ClienteAdmin)
