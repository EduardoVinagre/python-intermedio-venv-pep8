def get_unique_source(articles):
    """Extrae fuentes únicas de los artículos usando una comprehension"""
    return {article["source"]["name"] for article in articles}
