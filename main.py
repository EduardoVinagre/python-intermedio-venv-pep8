# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

from config import API_KEY_NEWS_API
from exceptions.api_key_error import APIKeyError
from news_api_client import fetch_news


# PEP 8: Funciones con nombres descriptivos y snake_case
def clean_text(text: str) -> str:
    # PEP 8: 4 espacios para indentación, no tabs
    """Limpia y normaliza el texto."""
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble línea en blanco entre funciones para separar lógicamente
def validate_api_key(api_key: str) -> bool:
    """Valida que la API key  tenga el formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fetch_news_from_api(api_name: str, query: str):
    """Obtiene noticias de una API específica."""
    pass


def process_article_data(raw_data):
    """Procesa los datos crudos de un artículo."""
    pass


# Longitud de línea: PEP 8 recomienda no exceder los 79 caracteres por línea
# Indentación: PEP 8 recomienda usar 4 espacios por nivel de indentación, no tabs
# Nombres descriptivos: PEP 8 recomienda usar nombres descriptivos para funciones, variables y clases snake_case
# Imports ordenados: estándar -> terceros -> locales, cada grupo separado por una línea en blanco
# Líneas en blanco: PEP 8 recomienda usar líneas en blanco para separar funciones y clases, y bloques de código dentro de funciones
# Comillas consistentes: PEP 8 recomienda usar comillas dobles para cadenas de texto, a menos que la cadena contenga comillas dobles, en cuyo caso se pueden usar comillas simples


response_data = None
try:
    response_data = fetch_news("newsapi", API_KEY_NEWS_API, query="Noticias de Python")
except APIKeyError as e:
    print(f"API Key error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

if response_data:
    for article in response_data["articles"]:
        print(article["title"])
