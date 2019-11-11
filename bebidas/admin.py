from django.contrib import admin

# Register your models here.
from .models import BebidaTamanhoBebida, TamanhoBebida, Bebida


class TamanhoBebidaInLine(admin.TabularInline):
    model = BebidaTamanhoBebida
    extra = 0

class BebidaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    ordering = ['nome']
    inlines = [TamanhoBebidaInLine]

admin.site.register(TamanhoBebida)
admin.site.register(Bebida, BebidaAdmin)
