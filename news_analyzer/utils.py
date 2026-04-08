def get_unique_source(articles):
    """Extrae fuentes únicas de los artículos usando una comprehension"""
    return {article["source"]["name"] for article in articles}


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    return list(
        filter(
            lambda article: article["source"]["name"].lower() == source.lower(),
            articles,
        )
    )


def get_reading_time(article: dict) -> dict:
    """Calcula el tiempo de lectura"""
    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article
