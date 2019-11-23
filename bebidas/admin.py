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
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    ordering = ['nome']
    inlines = [TamanhoBebidaInLine]


class TamanhoBebidaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nome']

admin.site.register(TamanhoBebida, TamanhoBebidaAdmin)
admin.site.register(Bebida, BebidaAdmin)
