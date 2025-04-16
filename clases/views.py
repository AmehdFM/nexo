from django.shortcuts import render, redirect
from django.http import Http404
from .services import (
    get_clases, 
    get_clase_by_slug, 
    get_temas_by_clase_id, 
    get_ejercicios_by_clase_id,
    get_recursos_by_clase_id,
    get_clases_relacionadas
)

def index(request):
    """
    Vista que muestra la lista de todas las clases disponibles,
    con opciones de filtrado.
    """
    # Obtener todos los objetos de Clase desde Supabase
    clases = get_clases()
    print(clases)
    
    # Aplicar filtros si vienen en la URL
    categoria = request.GET.get('categoria')
    nivel = request.GET.get('nivel')
    duracion = request.GET.get('duracion')
    
    # Filtrado manual - normalmente esto se haría en la consulta a Supabase
    # pero aquí lo hacemos en Python para simplificar
    if categoria:
        clases = [c for c in clases if c.get('categoria', '').lower() == categoria.lower()]
    
    if nivel:
        clases = [c for c in clases if c.get('nivel', '').lower() == nivel.lower()]
    
    if duracion:
        try:
            duracion_max = int(duracion)
            clases = [c for c in clases if c.get('duracion', 0) <= duracion_max]
        except ValueError:
            pass
    
    # Pasar los datos a la plantilla
    context = {
        'clases': clases,
        'active_page': 'clases',
    }
    
    return render(request, 'clases/index.html', context)

def detalle_clase(request, slug):
    """
    Vista que muestra los detalles de una clase específica
    identificada por su slug.
    """
    # Obtener la clase desde Supabase
    clase = get_clase_by_slug(slug)
    
    if not clase:
        raise Http404("La clase no existe")
    
    # Obtener temas, ejercicios y recursos relacionados
    temas = get_temas_by_clase_id(clase['id'])
    ejercicios = get_ejercicios_by_clase_id(clase['id'])
    recursos = get_recursos_by_clase_id(clase['id'])
    
    # Obtener clases relacionadas
    clases_relacionadas = get_clases_relacionadas(clase['categoria'], clase['id'])
    
    # Pasar todos los datos a la plantilla
    context = {
        'clase': clase,
        'temas': temas,
        'ejercicios': ejercicios,
        'recursos': recursos,
        'clases_relacionadas': clases_relacionadas,
        'active_page': 'clases',
    }
    
    return render(request, 'clases/detalle.html', context)