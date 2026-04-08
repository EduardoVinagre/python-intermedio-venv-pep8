def ejemplo_args(*args):
    return f"TODOS: {args}"


def custom_print(*args):
    print(f"Todos: {args}")
    print(type(args))


# custom_print(ejemplo_args("Este", "es", "un", "ejemplo", "de", "args"))
# custom_print(ejemplo_args("Hola", "mundo"))


def ejemplo_kwargs(**kwargs):
    print(f"KWARGS: {type(kwargs)}")
    print(f"KWARGS: {kwargs}")
    print("-" * 40)
    return f"KWARGS: {kwargs}"


ejemplo_kwargs(name="Ana", age=30, city="Madrid")
ejemplo_kwargs(name="Carlos", age=25, city="Barcelona", profession="Developer")

ejemplo_kwargs(
    api_key="DEMO",
    query="Noticias de Python",
    timeout=API_TIMEOUT_DEFAULT,
    retries=MAX_RETRIES_DEFAULT,
)
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN",
    section="technology",
    from_date="2024-01-01",
    timeout=API_TIMEOUT_DEFAULT,
    retries=MAX_RETRIES_DEFAULT,
)
