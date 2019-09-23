from django.contrib import admin

# Register your models here.
from django_reverse_admin import ReverseModelAdmin

from pyzza.models import TipoPizza, Ingrediente, SaborBorda, TamanhoPizza, SaborPizza, TamanhoBebida, Bebida, \
    Entregador, Cliente, StatusPedido, FormaDePagamento, BebidaTamanhoBebida, SaborPizzaIngrediente, \
    SaborBordaIngrediente, Pedido


class TipoPizzaAdmin(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(TipoPizza, TipoPizzaAdmin)

class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Ingrediente, IngredienteAdmin)

class BordaIngredienteInLine(admin.TabularInline):
    model = SaborBordaIngrediente
    extra = 0

class SaborBordaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome', 'valor_adicional']
    list_display_links = ['id', 'nome', 'valor_adicional']
    ordering = ['nome']
    inlines = [BordaIngredienteInLine]

admin.site.register(SaborBorda, SaborBordaAdmin)

class PizzaIngredienteInLine(admin.TabularInline):
    model = SaborPizzaIngrediente
    fields = ['ingrediente', 'quantidade']
    autocomplete_fields = ['ingrediente']
    extra = 0

class SaborPizzaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'tipo_pizza', 'nome', 'valor_adicional']
    list_display_links = ['id', 'tipo_pizza', 'nome', 'valor_adicional']
    ordering = ['nome']
    autocomplete_fields = ['tipo_pizza']
    inlines = [PizzaIngredienteInLine]
admin.site.register(SaborPizza, SaborPizzaAdmin)

admin.site.register(TamanhoPizza)
admin.site.register(TamanhoBebida)

class TamanhoBebidaInLine(admin.TabularInline):
    model = BebidaTamanhoBebida
    extra = 0

class BebidaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    ordering = ['nome']
    inlines = [TamanhoBebidaInLine]

admin.site.register(Bebida, BebidaAdmin)

class EntregadorAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    search_fields = ['nome']
    inline_reverse = [
        ('endereco', { 'fields': ['logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf']}),
    ]

admin.site.register(Entregador, EntregadorAdmin)

# class PaisAdmin(admin.ModelAdmin):
#     search_fields = ['nome']
#     inlines = [EstadoAdminInline]
#     list_display = ['id','nome']
#     list_editable = ['nome']
#     ordering = ['nome']
admin.site.register(Cliente)

admin.site.register(StatusPedido)
admin.site.register(FormaDePagamento)


admin.site.register(Pedido)
