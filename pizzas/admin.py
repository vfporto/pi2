from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TipoPizza, Ingrediente, SaborBordaIngrediente, SaborBorda, SaborPizzaIngrediente, SaborPizza, \
    TamanhoPizza


class TipoPizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'adicional_formatado', 'disponivel', 'ordem']
    list_display_links = ['id', 'nome']
    list_editable = ['ordem']
    search_fields = ['nome']
    list_filter = ['disponivel']
    actions = ['marcar_como_disponivel', 'marcar_como_indisponivel']

    def adicional_formatado(self, obj):
        return "R$ %7.2f" % obj.valor_adicional
    adicional_formatado.short_description = "Valor Adicional"

    def marcar_como_disponivel(self, request, queryset):
        queryset.update(disponivel=True)
    marcar_como_disponivel.short_description = "Marcar como disponível"

    def marcar_como_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
    marcar_como_indisponivel.short_description = "Marcar como não disponível"


class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome', 'qt_estoque', 'qt_minima', 'qt_maxima', 'un_medida']
    # list_display_links = ['nome', 'qt_estoque', 'qt_minima', 'qt_maxima', 'un_medida']
    list_display_links = ['id', 'nome']
    list_filter = ['un_medida']
    ordering = ['nome']
    list_editable = ['qt_estoque', 'qt_minima', 'qt_maxima']


class BordaIngredienteInLine(admin.TabularInline):
    model = SaborBordaIngrediente
    extra = 0


class SaborBordaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome', 'adicional_formatado', 'disponivel', 'ordem']
    list_display_links = ['id', 'nome']
    list_editable = ['ordem']
    ordering = ['ordem', 'nome']
    inlines = [BordaIngredienteInLine]
    list_filter = ['disponivel']
    actions = ['marcar_como_disponivel', 'marcar_como_indisponivel']

    def adicional_formatado(self, obj):
        return "R$ %7.2f" % obj.valor_adicional
    adicional_formatado.short_description = "Valor Adicional"

    def marcar_como_disponivel(self, request, queryset):
        queryset.update(disponivel=True)
    marcar_como_disponivel.short_description = "Marcar como disponível"

    def marcar_como_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
    marcar_como_indisponivel.short_description = "Marcar como não disponível"


class PizzaIngredienteInLine(admin.TabularInline):
    model = SaborPizzaIngrediente
    fields = ['ingrediente', 'quantidade', 'get_unidade_medida']
    readonly_fields = ['get_unidade_medida']
    autocomplete_fields = ['ingrediente']
    extra = 0

    def get_unidade_medida(self, obj):
        if (obj.ingrediente):
            return obj.ingrediente.un_medida
        else:
            return ""
    get_unidade_medida.short_description = "Unid. Medida"


class SaborPizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo_pizza', 'nome', 'adicional_formatado', 'disponivel']
    list_display_links = ['id', 'nome']
    # list_editable = ['disponivel']
    list_filter = ['tipo_pizza', 'disponivel']
    readonly_fields = ["show_imagem"]
    search_fields = ['tipo_pizza', 'nome']
    autocomplete_fields = ['tipo_pizza']
    inlines = [PizzaIngredienteInLine]
    ordering = ['tipo_pizza', 'nome']
    actions = ['marcar_como_disponivel', 'marcar_como_indisponivel']


    def show_imagem(self, obj):
        image_preview = ""
        try:
            image_preview = mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.imagem.url, width=obj.imagem.width, height=obj.imagem.height, ))
        except:
            image_preview = mark_safe('<b> Imagem não encontrada. Refazer upload </b>')
        return image_preview
    show_imagem.short_description = "Visualização"

    def adicional_formatado(self, obj):
        return "R$ %7.2f" % obj.valor_adicional
    adicional_formatado.short_description = "Valor Adicional"

    def marcar_como_disponivel(self, request, queryset):
        queryset.update(disponivel=True)
    marcar_como_disponivel.short_description = "Marcar como disponível"

    def marcar_como_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
    marcar_como_indisponivel.short_description = "Marcar como não disponível"


class TamanhoPizzaAdmin(admin.ModelAdmin):
    # list_display = ['id', 'nome', 'max_sabores', 'preco', 'multiplicador','disponivel','ordem']
    list_display = ['id', 'nome', 'max_sabores', 'preco_formatado', 'multiplicador','disponivel','ordem']
    list_display_links = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['disponivel']
    list_editable = ['ordem']
    actions = ['marcar_como_disponivel', 'marcar_como_indisponivel']

    def preco_formatado(self, obj):
        return "R$ %7.2f" % obj.preco
    preco_formatado.short_description = "Preço"

    def marcar_como_disponivel(self, request, queryset):
        queryset.update(disponivel=True)
    marcar_como_disponivel.short_description = "Marcar como disponível"

    def marcar_como_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
    marcar_como_indisponivel.short_description = "Marcar como não disponível"


admin.site.register(TipoPizza, TipoPizzaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(SaborBorda, SaborBordaAdmin)
admin.site.register(SaborPizza, SaborPizzaAdmin)
admin.site.register(TamanhoPizza, TamanhoPizzaAdmin)
