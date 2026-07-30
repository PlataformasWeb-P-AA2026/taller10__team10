from django.contrib import admin
from .models import Parroquia, Barrio, Presidente

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'ubicacion', 'tipo')

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia')
    search_fields = ('nombre', 'parroquia__nombre')

class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nickname', 'edad', 'profesion', 'barrio')
    search_fields = ('cedula', 'nickname', 'profesion', 'barrio__nombre')

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(Presidente, PresidenteAdmin)
