TITLE_LENGTH_THRESHOLD = 10

sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los títulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > TITLE_LENGTH_THRESHOLD:
            titles.append(article["title"])
    return titles


def extract_titles_comprehension(articles):
    """Extrae solo los títulos usando una comprehension"""
    return [
        article["title"]
        for article in articles
        if len(article["title"]) > TITLE_LENGTH_THRESHOLD
    ]


def extract_article_summaries(articles):
    """Extrae resúmenes de artículos con títulos largos usando una comprehension"""
    return {article["title"]: article["description"] for article in articles}


def extract_source_traditional(articles):
    """Extrae fuentes únicas de los artículos usando un for"""
    sources = set()
    for article in articles:
        sources.add(article["source"]["name"])
    return sources


def get_source(articles):
    """Extrae fuentes únicas de los artículos usando una comprehension"""
    return {article["source"]["name"] for article in articles}


def categorize_traditional(articles):
    """Categoriza artículos por categoría usando un for"""
    sources = get_source(articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []
        for article in articles:
            if article["source"]["name"] == source:
                results[source].append(article)
    return results


def categorize(articles):
    """Categoriza artículos por categoría usando una comprehension"""
    sources = get_source(articles)
    return {
        source: [article for article in articles if article["source"]["name"] == source]
        for source in sources
    }


# print(extract_titles_traditional(sample_articles))
# print("=" * 122)
# print(extract_titles_comprehension(sample_articles))
# print(extract_article_summaries(sample_articles))
# print("=" * 122)
# print(extract_source_traditional(sample_articles))
# print("=" * 122)
# print(get_source(sample_articles))
print(categorize_traditional(sample_articles))
print("=" * 122)
print(categorize(sample_articles))
