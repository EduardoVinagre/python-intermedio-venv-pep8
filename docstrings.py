"""
Explicación de docstrings.

En esta clase puedo explicar cómo funcionan los docstrings en Python

"""


def ejemplo_sin_docstring():
    return "Hola, mundo!"


def ejemplo_con_docstring():
    """
    DESCRIPTION
    ARGS
    RETURNS
    EXCEPTIONS
    EXAMPLES
    Esta función devuelve un saludo.

    Returns:
        str: Un saludo en español
    """
    return "Hola, mundo!"


print(ejemplo_con_docstring.__doc__)
help(ejemplo_con_docstring)
