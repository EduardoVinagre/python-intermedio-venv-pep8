import json
import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv

from exceptions.api_key_error import APIKeyError

# Cargar variables de entorno
load_dotenv()

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT_DEFAULT: int = int(os.getenv("API_TIMEOUT_DEFAULT", 30))
MAX_RETRIES_DEFAULT: int = int(os.getenv("MAX_RETRIES_DEFAULT", 3))
DEFAULT_LANGUAGE: str = "es"  # PEP 8: Uso de comillas dobles para cadenas de texto
BASE_URL: str | None = os.getenv("BASE_URL")


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
