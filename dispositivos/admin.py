from django.contrib import admin

# Register your models here.

from .models import Categoria, Zona, Dispositivo, Medicion, Alerta

admin.site.register([Categoria, Zona, Medicion, Alerta])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre_dispositivo','categoria','zona','marca','modelo')
    list_filter = ('categoria',)
    search_fields = ('nombre',)