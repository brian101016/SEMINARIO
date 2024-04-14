contactos = []


def agregar_contacto():
    nombre = input("    Ingrese el nombre del contacto: ")
    telefono = input("    Ingrese el numero de telefono: ")
    contactos.append({ "nombre": nombre, "telefono": telefono })
    print(f"    Contacto {nombre} agregado con exito.")


def buscar_contacto():
    find_name = input("    Ingrese el nombre a buscar: ")
    found = False
    for contacto in contactos:
      if contacto["nombre"] == find_name:
        print("    Se ha encontrado un contacto:")
        print(f"    -> Nombre: {find_name}")
        print(f"    -> Telefono: {contacto["telefono"]}")
        found = True
        break
    if not found: print(f"    No se ha encontrado a '{find_name}'")


def eliminar_contacto():
    find_name = input("    Ingrese el nombre a eliminar: ")
    found = False
    index = -1
    for contacto in contactos:
      index += 1
      if contacto["nombre"] == find_name:
        print(f"    Se ha eliminado a {find_name}")
        del contactos[index]
        found = True
        break
    if not found: print(f"    No existe '{find_name}'")


opcion = 1

while opcion != 4:
    print("\nMenu:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opcion = int(input("Ingrese el numero de la opcion deseada: "))

    print("")
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        eliminar_contacto()
    elif opcion == 4:
        print("    Saliendo...")
    else:
        print("    Ingrese una opcion valida")
