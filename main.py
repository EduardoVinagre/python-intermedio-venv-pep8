# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

from exceptions.api_key_error import APIKeyError
from news_analyzer.config import API_KEY_NEWS_API
from news_analyzer.news_api_client import fetch_news
from news_analyzer.utils import (
    get_articles_by_source,
    get_reading_time,
    get_unique_source,
)
from news_analyzer.open_ai import analyze_news_with_ia

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
    # source_set = get_unique_source(response_data["articles"])
    # for index, source in enumerate(source_set, start=1):
    #     print(f"No. {index} -- {source}")

    # for article in response_data["articles"]:
    #     print(article["source"])

    # geeksroom_articles = get_articles_by_source(
    #     response_data["articles"], "Geeksroom.com"
    # )

    # for article in geeksroom_articles:
    #     print(article["source"]["name"], article["title"])

    # articles = list(map(get_reading_time, response_data["articles"]))
    # print(articles[0])
    analyze_news_with_ia(response_data['articles'], "Qué piensas de Python?")