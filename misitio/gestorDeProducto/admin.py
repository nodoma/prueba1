from django.contrib import admin
from .models import Producto
from .models import Marca
# Register your models here.

class productoAdmin(admin.ModelAdmin):
    list_display    =['codigo','descripcion','stock','precioCosto','precioVenta']

    list_display_links = ['codigo','descripcion']

    list_filter     =['descripcion']

    search_fields   =['codigo', 'descripcion']
admin.site.register(Producto, productoAdmin)

class marcaAdmin(admin.ModelAdmin):
    list_display    = ['nombre', 'activo']
    list_filter     = ['nombre']
    search_fields   =['nombre']

admin.site.register(Marca, marcaAdmin)

