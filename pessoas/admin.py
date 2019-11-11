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
        ('endereco', {'fields': ['logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf']}),
    ]


class ClienteAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    search_fields = ['nome']
    inline_reverse = [
        ('endereco', {'fields': ['logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf']}),
    ]


admin.site.register(Entregador, EntregadorAdmin)
admin.site.register(Cliente, ClienteAdmin)
