tareas = []


def crear_tarea():
    nombre = input("    Nombre de la tarea: ")
    tareas.append(nombre)
    print("    Agregada con exito.")


def completar_tarea():
    mostrar_pendientes()

    index = int(input("\n    Ingrese el numero de la tarea a completar: "))
    nombre = tareas[index]
    del tareas[index]
    print(f"    Se ha completado '{nombre}'")


def mostrar_pendientes():
    print("    Tareas pendientes:")
    for i in range(len(tareas)):
        print(f"    {i}.- {tareas[i]}")


opcion = 1

while opcion != 4:
    print("\nMenu:")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas pendientes")
    print("4. Salir")
    opcion = int(input("Ingrese el numero de la opcion deseada: "))

    print("")
    if opcion == 1:
        crear_tarea()
    elif opcion == 2:
        completar_tarea()
    elif opcion == 3:
        mostrar_pendientes()
    elif opcion == 4:
        print("    Saliendo...")
    else:
        print("    Ingrese una opcion valida")
