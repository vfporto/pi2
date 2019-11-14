from django.contrib import admin

from pedidos.models import ItemPizza, StatusPedido, FormaDePagamento, Pedido, ItemBebida


class ItemPizzaInline(admin.TabularInline):
    model = ItemPizza
    extra = 0
    fields = ['tamanho_pizza', 'sabor_borda', 'sabores', 'quantidade', 'get_preco']
    readonly_fields = ['get_preco']
    autocomplete_fields = ['sabores']


class ItemBebidaInline(admin.TabularInline):
    model = ItemBebida
    extra = 0
    fields = ['id','bebida_tamanho' , 'quantidade', 'preco', 'get_preco']
    readonly_fields = ['get_preco']

"""
    quantidade = models.PositiveIntegerField(null=False, default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_bebida')
    # bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    bebida_tamanho = models.ForeignKey(BebidaTamanhoBebida, on_delete=models.PROTECT)
"""


class PedidoAdmin(admin.ModelAdmin):
    # search_fields = ['']
    list_display = ['id', 'data', 'cliente', 'status_pedido', 'get_total']
    list_display_links = ['id', 'data', 'cliente','get_total', 'status_pedido']
    ordering = ['data']
    readonly_fields = ['get_total']
    inlines = [ItemPizzaInline, ItemBebidaInline]


admin.site.register(StatusPedido)
admin.site.register(FormaDePagamento)
admin.site.register(Pedido, PedidoAdmin)
