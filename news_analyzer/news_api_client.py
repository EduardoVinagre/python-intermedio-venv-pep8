import json
import urllib.parse
import urllib.request
from typing import Callable

from dotenv import load_dotenv

from exceptions.api_key_error import APIKeyError
from news_analyzer.config import API_TIMEOUT_DEFAULT, BASE_URL, MAX_RETRIES_DEFAULT

# Cargar variables de entorno
load_dotenv()


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


def guardian_client(
    api_key: str,
    section: str,
    from_date: str,
    timeout: int = API_TIMEOUT_DEFAULT,
    retries: int = MAX_RETRIES_DEFAULT,
):
    return f"The Guardian: api_key={api_key}, section={section}, from_date={from_date}, timeout={timeout}, retries={retries}"


def newsapi_client(
    api_key: str,
    query: str,
    timeout: int = API_TIMEOUT_DEFAULT,
    retries: int = MAX_RETRIES_DEFAULT,
):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        raise APIKeyError(f"HTTP error occurred: {e.code} - {e.reason}")

    # if response.status_code != 200:
    #     raise Exception(f"Error al conectar con NewsAPI: {response.status_code}")
    # print(response.json())
    # return f"Conectando a NewsAPI con api_key={api_key}, query={query}, timeout={timeout}, retries={retries}"


def fetch_news(api_name: str, *args, **kwargs):
    """
    Función flexible para conectar con la API
    """

    base_config: dict = {
        "timeout": API_TIMEOUT_DEFAULT,
        "retries": MAX_RETRIES_DEFAULT,
    }
    config: dict = {
        **base_config,
        **kwargs,
    }  # Combina la configuración base con los kwargs específicos

    api_clients: dict = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    client: Callable = api_clients[api_name]
    return client(*args, **config)
