from django.contrib import admin
from .models import Clase, Objetivo, Requisito, Tema, Ejercicio, Recurso, Enlace

class ObjetivoInline(admin.TabularInline):
    model = Objetivo
    extra = 1

class RequisitoInline(admin.TabularInline):
    model = Requisito
    extra = 1

class TemaInline(admin.TabularInline):
    model = Tema
    extra = 1

class EjercicioInline(admin.TabularInline):
    model = Ejercicio
    extra = 1

class RecursoInline(admin.TabularInline):
    model = Recurso
    extra = 1

class EnlaceInline(admin.TabularInline):
    model = Enlace
    extra = 1

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'nivel', 'duracion', 'profesor', 'fecha_actualizacion')
    list_filter = ('categoria', 'nivel')
    search_fields = ('titulo', 'descripcion', 'profesor')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [ObjetivoInline, RequisitoInline, TemaInline, EjercicioInline, RecursoInline, EnlaceInline]

# También puedes registrar los otros modelos si necesitas administrarlos independientemente
admin.site.register(Tema)
admin.site.register(Ejercicio)
admin.site.register(Recurso)
admin.site.register(Enlace)