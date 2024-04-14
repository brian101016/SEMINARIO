# Importar date para trabajar con el año actual
from datetime import date

# Declarar las variables junto a su tipo de dato
nombre: str = ""
edad: int = 0
altura: float = 0

# Solicitar la información
nombre = input("Ingrese su nombre: ")
# Convertir a tipo numérico entero
edad = int(input("Ingrese su edad: "))
# Convertir a tipo numérico flotante
altura = float(input("Ingrese su altura en metros: "))

# Mostrar la información obtenida
print("\nResumen de la información:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")

# Calcular el año de nacimiento
# Fórmula: año actual - edad (inferir tipo de dato entero)
nacimiento = (date.today().year) - edad
print(f"Año de nacimiento: {nacimiento}")

# Calcular a futuro en 5 años
print(f"\nEn 5 años, tendrás {edad + 5} años.")
