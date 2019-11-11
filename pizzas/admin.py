from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TipoPizza, Ingrediente, SaborBordaIngrediente, SaborBorda, SaborPizzaIngrediente, SaborPizza, \
    TamanhoPizza


class TipoPizzaAdmin(admin.ModelAdmin):
    search_fields = ['nome']


class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']


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


class PizzaIngredienteInLine(admin.TabularInline):
    model = SaborPizzaIngrediente
    fields = ['ingrediente', 'quantidade']
    autocomplete_fields = ['ingrediente']
    extra = 0


class SaborPizzaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'tipo_pizza', 'nome', 'valor_adicional', 'disponivel']
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


admin.site.register(TipoPizza, TipoPizzaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(SaborBorda, SaborBordaAdmin)
admin.site.register(SaborPizza, SaborPizzaAdmin)
admin.site.register(TamanhoPizza)
