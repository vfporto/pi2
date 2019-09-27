from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from django_reverse_admin import ReverseModelAdmin

from pyzza.models import TipoPizza, Ingrediente, SaborBorda, TamanhoPizza, SaborPizza, TamanhoBebida, Bebida, \
    Entregador, Cliente, StatusPedido, FormaDePagamento, BebidaTamanhoBebida, SaborPizzaIngrediente, \
    SaborBordaIngrediente, Pedido, ItemPizza


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
    list_display = ['id', 'nome', 'valor_adicional', 'disponivel']
    list_display_links = ['id', 'nome', 'valor_adicional']
    list_editable = ['disponivel']
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
    list_display = ['id', 'tipo_pizza', 'nome', 'valor_adicional','disponivel']
    list_display_links = ['id', 'tipo_pizza', 'nome', 'valor_adicional']
    list_editable = ['disponivel']
    readonly_fields = ["show_imagem"]
    ordering = ['nome']
    autocomplete_fields = ['tipo_pizza']
    inlines = [PizzaIngredienteInLine]

    def show_imagem(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.imagem.url,
            width=obj.imagem.width,
            height=obj.imagem.height,
        )
    )

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

class ClienteAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    search_fields = ['nome']
    inline_reverse = [
        ('endereco', { 'fields': ['logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf']}),
    ]
admin.site.register(Cliente, ClienteAdmin)


admin.site.register(StatusPedido)
admin.site.register(FormaDePagamento)

class ItemPizzaInline(admin.StackedInline):
    model = ItemPizza
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    #search_fields = ['']
    list_display = ['id', 'data', 'cliente', 'status_pedido']
    list_display_links = ['id', 'data', 'cliente', 'status_pedido']
    ordering = ['data']
    inlines = [ItemPizzaInline]

admin.site.register(Pedido, PedidoAdmin)
