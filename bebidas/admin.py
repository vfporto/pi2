from django.contrib import admin

# Register your models here.
from .models import BebidaTamanhoBebida, TamanhoBebida, Bebida


class TamanhoBebidaInLine(admin.TabularInline):
    model = BebidaTamanhoBebida
    autocomplete_fields = ['tamanho_bebida']
    fields = ['tamanho_bebida', 'preco', 'disponivel']
    extra = 0

class BebidaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome', 'disponivel']
    list_display_links = ['id', 'nome']
    # list_editable = ['disponivel']
    ordering = ['nome']
    inlines = [TamanhoBebidaInLine]
    actions = ['marcar_como_disponivel', 'marcar_como_indisponivel']

    def marcar_como_disponivel(self, request, queryset):
        queryset.update(disponivel=True)
    marcar_como_disponivel.short_description = "Marcar como disponível"

    def marcar_como_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
    marcar_como_indisponivel.short_description = "Marcar como não disponível"


class TamanhoBebidaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nome']
    list_display = ['id', 'nome', 'disponivel', 'ordem']
    list_display_links = ['id', 'nome']
    list_editable = ['ordem']
    ordering = ['ordem']
    actions = ['marcar_como_disponivel', 'marcar_como_indisponivel']

    def marcar_como_disponivel(self, request, queryset):
        queryset.update(disponivel=True)
    marcar_como_disponivel.short_description = "Marcar como disponível"

    def marcar_como_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
    marcar_como_indisponivel.short_description = "Marcar como não disponível"





admin.site.register(TamanhoBebida, TamanhoBebidaAdmin)
admin.site.register(Bebida, BebidaAdmin)
