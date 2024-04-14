# Importar modulo para numeros aleatorios
from random import randint

# Mostrar comienzo del juego
print("Juego de adivinanza")

# Bandera para saber si el usuario quiere seguir jugando
seguir_jugando = "S"

while seguir_jugando == "S":

    print("\nIntenta adivinar un numero del 1 al 100")

    # Generar numero aleatorio objetivo y variables
    objetivo = randint(1, 100)
    intentos = 1
    seleccionado = int(input("Ingresa tu intento: "))

    while seleccionado != objetivo:
        if seleccionado > objetivo:
            print("El numero objetivo es menor. Intenta de nuevo.")
        else:
            print("El numero objetivo es mayor. Intenta de nuevo.")

        intentos += 1
        seleccionado = int(input("Ingresa tu intento: "))

    print(
        f"Felicidades, adivinaste el numero secreto {objetivo} en {intentos} intentos."
    )
    seguir_jugando = input("Quieres volver a jugar? S/N: ")
