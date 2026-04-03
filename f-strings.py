name = "Ana"
year = 2020
text = f"Hola, {name}! Bienvenido al sistema de análisis de noticias."
print(text)
text_2 = "Hola"
print(text_2)

# format es mas difícil de leer y más propenso a errores, especialmente con múltiples variables o formatos complejos. Las f-strings son más claras y concisas, lo que mejora la legibilidad del código.
text_format = "Hola {0}! Bienvenido al sistema de análisis de noticias.".format(name)
print(text_format)

text_suma = f"El resultado de 2 + 2 es {2 + 2}."
print(text_suma)

text_calculo = f"Hola, {name}, tu edad es: {2025 - year} años"
print(text_calculo)

text_func = f"HOLA {name.upper()}!"
print(text_func)

edad = 20
text_if = (
    f"Hola {name}, {'eres mayor de edad' if edad >= 18 else 'eres menor de edad'}."
)

print(text_if)

text_if_2 = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad."
print(text_if_2)
