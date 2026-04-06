def sum_args(*args):
    """Suma una cantidad variable de argumentos numéricos."""
    return sum(args)


def sum_args_traditional(*args):
    """Suma una cantidad variable de argumentos numéricos usando un bucle tradicional."""
    total = 0
    for num in args:
        if type(num) is int or type(num) is float:
            total += num
    return total


def imprime_resultado(resultado):
    """Imprime el resultado de la suma."""
    print(f"El resultado de la suma es: {resultado}")


imprime_resultado(sum_args(1, 2, 3, 4, 5))
imprime_resultado(sum_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
imprime_resultado(sum_args_traditional(1, 2, "hola", 3, 4, 5))
imprime_resultado(sum_args_traditional(1, 2, 3, "", 4, 5, 6, 7, 8, 9, 10))
