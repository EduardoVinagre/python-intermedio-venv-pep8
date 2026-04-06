import os

import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT_DEFAULT = int(os.getenv("API_TIMEOUT_DEFAULT", 30))
MAX_RETRIES_DEFAULT = int(os.getenv("MAX_RETRIES_DEFAULT", 3))
DEFAULT_LANGUAGE = "es"  # PEP 8: Uso de comillas dobles para cadenas de texto

url_template = os.getenv("URL_TEMPLATE")
api_key_news_api = os.getenv("API_KEY_NEWS_API")

print(f"URL Template: {url_template}")
print(f"API Key News API: {api_key_news_api}")


# PEP 8: Funciones con nombres descriptivos y snake_case
def clean_text(text):
    # PEP 8: 4 espacios para indentación, no tabs
    """Limpia y normaliza el texto."""
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble línea en blanco entre funciones para separar lógicamente
def validate_api_key(api_key):
    """Valida que la API key  tenga el formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fetch_news_from_api(api_name, query):
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


def newsapi_client(
    api_key, query, timeout=API_TIMEOUT_DEFAULT, retries=MAX_RETRIES_DEFAULT
):
    print(
        f"Conectando a NewsAPI con api_key={api_key}, query={query}, timeout={timeout}, retries={retries}"
    )
    response = requests.get(url_template.format(query, api_key), timeout=timeout)
    if response.status_code != 200:
        raise Exception(f"Error al conectar con NewsAPI: {response.status_code}")
    print(response.json())
    return response.json()


def guardian_client(
    api_key,
    section,
    from_date,
    timeout=API_TIMEOUT_DEFAULT,
    retries=MAX_RETRIES_DEFAULT,
):
    return f"The Guardian: api_key={api_key}, section={section}, from_date={from_date}, timeout={timeout}, retries={retries}"


def ejemplo_args(*args):
    return f"TODOS: {args}"


def custom_print(*args):
    print(f"Todos: {args}")
    print(type(args))


custom_print(ejemplo_args("Este", "es", "un", "ejemplo", "de", "args"))
custom_print(ejemplo_args("Hola", "mundo"))


def ejemplo_kwargs(**kwargs):
    print(f"KWARGS: {type(kwargs)}")
    print(f"KWARGS: {kwargs}")
    print("-" * 40)
    return f"KWARGS: {kwargs}"


ejemplo_kwargs(name="Ana", age=30, city="Madrid")
ejemplo_kwargs(name="Carlos", age=25, city="Barcelona", profession="Developer")

ejemplo_kwargs(
    api_key="DEMO",
    query="Noticias de Python",
    timeout=API_TIMEOUT_DEFAULT,
    retries=MAX_RETRIES_DEFAULT,
)
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN",
    section="technology",
    from_date="2024-01-01",
    timeout=API_TIMEOUT_DEFAULT,
    retries=MAX_RETRIES_DEFAULT,
)


def fetch_news(api_name, *args, **kwargs):
    """
    Función flexible para conectar con la API
    """

    base_config = {
        "timeout": API_TIMEOUT_DEFAULT,
        "retries": MAX_RETRIES_DEFAULT,
    }
    config = {
        **base_config,
        **kwargs,
    }  # Combina la configuración base con los kwargs específicos

    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)


fetch_news("newsapi", api_key_news_api, query="Noticias de Python")
