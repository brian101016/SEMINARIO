print("############################################# Ejercicio 1 ")

# Obtener datos
producto1 = int(input("Ingrese la cantidad de Producto 1 que desea comprar: "))
producto2 = int(input("Ingrese la cantidad de Producto 2 que desea comprar: "))
producto3 = int(input("Ingrese la cantidad de Producto 3 que desea comprar: "))

# Valores de los precios
valor_1: float = 10.5
valor_2: float = 5.75
valor_3: float = 8.00

# Mostrar
print("\nDetalle de la compra: ")
print(f"Producto 1 - Cantidad: {producto1} x costo: {valor_1} = ${producto1 * valor_1}")
print(f"Producto 2 - Cantidad: {producto2} x costo: {valor_2} = ${producto2 * valor_2}")
print(f"Producto 3 - Cantidad: {producto3} x costo: {valor_3} = ${producto3 * valor_3}")

# Suma
total_compra: float = (
    (producto1 * valor_1) + (producto2 * valor_2) + (producto3 * valor_3)
)

print("------------------------------")
print(f"Costo Total de la Compra: ${total_compra}")

print("\n############################################# Ejercicio 2 ")

# Obtener datos
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Calcular
area: float = longitud * ancho
perimetro: float = (longitud * 2) + (ancho * 2)

# Mostrar
print("Resultados:")
print(f"Área del rectángulo: {area}")
print(f"Perímetro del rectángulo: {perimetro}")

print("\n############################################# Ejercicio 3 ")

# Obtener datos
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

# Calcular
print("Resultados: ")
print(f"Suma: {n1 + n2}")
print(f"Resta: {n1 - n2}")
print(f"Multiplicación: {n1 * n2}")

# Verficiar 0
if n2 == 0:
    print("No es posible dividir por 0!")
else:
    print(f"División: {n1 / n2}")
