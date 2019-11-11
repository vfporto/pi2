from django.contrib import admin

from pedidos.models import ItemPizza, StatusPedido, FormaDePagamento, Pedido, ItemBebida


class ItemPizzaInline(admin.StackedInline):
    model = ItemPizza
    extra = 0
    fields = ['tamanho_pizza', 'sabor_borda', 'sabores', 'observacao', 'quantidade', 'preco']
    autocomplete_fields = ['sabores']


class ItemBebidaInline(admin.StackedInline):
    model = ItemBebida
    extra = 0
    fields = ['id','bebida_tamanho' , 'quantidade', 'preco']
"""
    quantidade = models.PositiveIntegerField(null=False, default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_bebida')
    # bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT)
    bebida_tamanho = models.ForeignKey(BebidaTamanhoBebida, on_delete=models.PROTECT)
"""


class PedidoAdmin(admin.ModelAdmin):
    # search_fields = ['']
    list_display = ['id', 'data', 'cliente', 'status_pedido']
    list_display_links = ['id', 'data', 'cliente', 'status_pedido']
    ordering = ['data']
    inlines = [ItemPizzaInline, ItemBebidaInline]


admin.site.register(StatusPedido)
admin.site.register(FormaDePagamento)
admin.site.register(Pedido, PedidoAdmin)
