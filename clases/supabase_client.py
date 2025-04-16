import os
from supabase import create_client
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de Supabase
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

# Crear cliente Supabase
supabase = create_client(supabase_url, supabase_key)

def get_supabase_client():
    """Retorna el cliente Supabase para ser usado en otras partes de la aplicación"""
    supabase = create_client(supabase_url, supabase_key)
    return supabase