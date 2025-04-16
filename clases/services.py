from .supabase_client import get_supabase_client

def get_clases():
    """Obtiene todas las clases disponibles de Supabase"""
    supabase = get_supabase_client()

    
    # Realiza la consulta - ajusta el nombre de la tabla según tu estructura en Supabase
    response = supabase.table('clases').select('*').execute()
    print(response)
    # Retorna los datos
    return response.data

def get_clase_by_slug(slug):
    """Obtiene una clase específica por su slug"""
    supabase = get_supabase_client()
    
    # Consulta para obtener una clase por su slug
    response = supabase.table('clases').select('*').eq('slug', slug).execute()
    
    # Si hay resultados, retorna el primero
    if response.data:
        return response.data[0]
    return None

def get_temas_by_clase_id(clase_id):
    """Obtiene todos los temas asociados a una clase"""
    supabase = get_supabase_client()
    
    # Consulta para obtener temas de una clase
    response = supabase.table('temas').select('*').eq('clase_id', clase_id).order('orden').execute()
    
    return response.data

def get_ejercicios_by_clase_id(clase_id):
    """Obtiene todos los ejercicios asociados a una clase"""
    supabase = get_supabase_client()
    
    # Consulta para obtener ejercicios de una clase
    response = supabase.table('ejercicios').select('*').eq('clase_id', clase_id).execute()
    
    return response.data

def get_recursos_by_clase_id(clase_id):
    """Obtiene todos los recursos asociados a una clase"""
    supabase = get_supabase_client()
    
    # Consulta para obtener recursos de una clase
    response = supabase.table('recursos').select('*').eq('clase_id', clase_id).execute()
    
    return response.data

def get_clases_relacionadas(categoria, exclude_id):
    """Obtiene clases relacionadas por categoría, excluyendo una clase específica"""
    supabase = get_supabase_client()
    
    # Consulta para obtener clases relacionadas
    response = supabase.table('clases').select('*').eq('categoria', categoria).neq('id', exclude_id).limit(4).execute()
    
    return response.data