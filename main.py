# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT_DEFAULT = 30
MAX_RETRIES_DEFAULT = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Uso de comillas dobles para cadenas de texto


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
    return f"NewsAPI: api_key={api_key}, query={query}, timeout={timeout}, retries={retries}"


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
custom_print(ejemplo_args())
