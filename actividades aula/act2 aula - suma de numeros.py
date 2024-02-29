# Declarar la lista de numeros y variable de total
lista = [1, 2, 3, 4, 5]
total: float = 0

# Mostrar la lista de numeros antes de la suma
print(f"Lista de numeros a sumar: {lista}")

# Ciclo para iterar sobre la lista
for num in lista:
    # Incrementar el numero actual con el total almacenado
    total += num

# Mostrar el resultado final
print(f"Resultado final: {total}")
