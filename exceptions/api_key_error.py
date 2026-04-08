##from news_system_error import NewsSystemError
class NewsSystemError(Exception):
    """Base class for exceptions in this module."""

    pass


class APIKeyError(NewsSystemError):
    """Exception raised for errors in the API key."""

    pass
