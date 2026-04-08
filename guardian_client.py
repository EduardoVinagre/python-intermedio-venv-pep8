import os

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT_DEFAULT: int = int(os.getenv("API_TIMEOUT_DEFAULT", 30))
MAX_RETRIES_DEFAULT: int = int(os.getenv("MAX_RETRIES_DEFAULT", 3))
DEFAULT_LANGUAGE: str = "es"  # PEP 8: Uso de comillas dobles para cadenas de texto
BASE_URL: str | None = os.getenv("BASE_URL")


def guardian_client(
    api_key: str,
    section: str,
    from_date: str,
    timeout: str = API_TIMEOUT_DEFAULT,
    retries: str = MAX_RETRIES_DEFAULT,
):
    return f"The Guardian: api_key={api_key}, section={section}, from_date={from_date}, timeout={timeout}, retries={retries}"
