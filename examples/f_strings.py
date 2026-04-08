import locale
from datetime import datetime

try:
    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
except locale.Error:
    print("La configuración regional 'es_ES' no está disponible en este sistema.")

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

bank_balance = 1200000000
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text)

stock_price = 1234.56789
text = f"El precio de la acción es: {stock_price:.2f}"
print(text)

user_id = 1
text = f"El ID del usuario es: {user_id:04d}"
print(text)


product = "Laptop"
price = 1000

text = f"Producto: {product:>15} | ${price:>15,.2f}"
print(text)
text = f"Producto: {product:<15} | ${price:<15,.2f}"
print(text)
print(f"{text}\n{text}")


fecha = datetime(2024, 6, 1)
text = f"La fecha completa es: {fecha}"
print(text)
text = f"La fecha formateada es: {fecha:%A %d de %B de %Y a las %I:%M %p}"
print(text)

ahora = datetime.now()

# Formatear la fecha
# %A: Día completo, %d: Día número, %B: Mes completo, %Y: Año, %I: Hora (12h), %M: Minutos, %p: AM/PM
formato = ahora.strftime("%A %d de %B de %Y a las %I:%M %p")

print(formato)
