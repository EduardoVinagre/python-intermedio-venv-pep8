numeros = [1, 2, 3, 4, 5]
cuadrados = []

for num in numeros:
    cuadrados.append(num**2)

print(numeros)
print(cuadrados)


def cuadrado(num):
    return num**2


cuadrados_map = list(map(cuadrado, numeros))
print(cuadrados_map)
