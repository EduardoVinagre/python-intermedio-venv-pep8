import os

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT_DEFAULT: int = int(os.getenv("API_TIMEOUT_DEFAULT", 30))
MAX_RETRIES_DEFAULT: int = int(os.getenv("MAX_RETRIES_DEFAULT", 3))
DEFAULT_LANGUAGE: str = "es"  # PEP 8: Uso de comillas dobles para cadenas de texto
BASE_URL: str | None = os.getenv("BASE_URL")

url_template: str | None = os.getenv("URL_TEMPLATE")
API_KEY_NEWS_API: str | None = os.getenv("API_KEY_NEWS_API")