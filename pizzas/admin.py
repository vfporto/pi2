from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TipoPizza, Ingrediente, SaborBordaIngrediente, SaborBorda, SaborPizzaIngrediente, SaborPizza, \
    TamanhoPizza


class TipoPizzaAdmin(admin.ModelAdmin):
    search_fields = ['nome']


class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome', 'qt_estoque', 'qt_minima', 'qt_maxima', 'un_medida']
    # list_display_links = ['nome', 'qt_estoque', 'qt_minima', 'qt_maxima', 'un_medida']
    list_display_links = ['id', 'nome']
    ordering = ['nome']
    list_editable = ['qt_estoque', 'qt_minima', 'qt_maxima', 'un_medida']


class BordaIngredienteInLine(admin.TabularInline):
    model = SaborBordaIngrediente
    extra = 0


class SaborBordaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome', 'valor_adicional', 'disponivel', 'ordem']
    list_display_links = ['id', 'nome', 'valor_adicional']
    list_editable = ['disponivel', 'ordem']
    ordering = ['ordem', 'nome']
    inlines = [BordaIngredienteInLine]


class PizzaIngredienteInLine(admin.TabularInline):
    model = SaborPizzaIngrediente
    fields = ['ingrediente', 'quantidade']
    autocomplete_fields = ['ingrediente']
    extra = 0


class SaborPizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo_pizza', 'nome', 'valor_adicional', 'disponivel']
    list_display_links = ['id', 'tipo_pizza', 'nome', 'valor_adicional']
    list_editable = ['disponivel']
    list_filter = ['tipo_pizza']
    readonly_fields = ["show_imagem"]
    search_fields = ['nome']
    autocomplete_fields = ['tipo_pizza']
    inlines = [PizzaIngredienteInLine]
    ordering = ['nome']

    def show_imagem(self, obj):
        image_preview = ""
        try:
            image_preview = mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.imagem.url, width=obj.imagem.width, height=obj.imagem.height, ))
        except:
            image_preview = mark_safe('<b> Imagem não encontrada. Refazer upload </b>')
        return image_preview

    show_imagem.short_description = "Visualização"

class TamanhoPizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'max_sabores', 'preco', 'multiplicador','ordem']
    list_display_links = ['id', 'nome', 'max_sabores', 'preco', 'multiplicador']
    search_fields = ['nome']
    list_editable = ['ordem']


admin.site.register(TipoPizza, TipoPizzaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(SaborBorda, SaborBordaAdmin)
admin.site.register(SaborPizza, SaborPizzaAdmin)
admin.site.register(TamanhoPizza, TamanhoPizzaAdmin)
