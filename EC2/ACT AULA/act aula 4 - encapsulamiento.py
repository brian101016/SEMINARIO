class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        if validar_string(valor):
            self._nombre = valor

    def get_edad(self):
        return self._edad

    def set_edad(self, valor):
        if validar_edad(valor):
            self._edad = valor


class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self._cargo = cargo

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, valor):
        if validar_cargo(valor):
            self._cargo = valor

    def imprimir_detalles(self):
        print("Datos del empleado:\n"
              f"Nombre: {self.get_nombre()}\n"
              f"Edad: {self.get_edad()}\n"
              f"Cargo: {self.get_cargo()}\n")


def validar_string(valor):
    if isinstance(valor, str) and valor != "":
        return True
    else:
        print("Ingresa una cadena valida!")
        return False


def validar_edad(valor):
    if isinstance(valor, int) and (0 < valor <= 150):
        return True
    else:
        print("Ingresa un numero entero valido entre 1-150!")
        return False


def validar_cargo(valor):
    if validar_string(valor) and (valor in cargos):
        return True
    else:
        print("Ingresa un cargo valido entre", cargos)
        return False


# Funcion que intenta convertir un numero en entero, previene errores
# y si falla, regresa 0 como numero default
def convertir_entero(valor):
    try:
        resultado = int(valor)
        return resultado
    except ValueError:
        # Mensaje opcional
        # print("Error al convertir, marcando 0 como default")
        return 0  # Default a 0 cuando haya error


# VARIABLES GLOBALES
cargos = ["Analista", "Desarrollador", "Tester"]
# Creamos uno con info default, pero despues la cambiamos
empleado1 = Empleado("Nuevo nombre", 1, "Analista")


# Shortcut para capturar mas rapido sin duplicar codigo
def capturar_datos():
    # CAPTURAR DATOS
    while True:
        nuevo_nombre = input("Nombre del empleado: ")
        if validar_string(nuevo_nombre):
            empleado1.set_nombre(nuevo_nombre)
            break

    while True:
        nueva_edad = convertir_entero(input("Edad del empleado: "))
        if validar_edad(nueva_edad):
            empleado1.set_edad(nueva_edad)
            break

    while True:
        nuevo_cargo = input("Cargo del empleado: ")
        if validar_cargo(nuevo_cargo):
            empleado1.set_cargo(nuevo_cargo)
            break


capturar_datos()
empleado1.imprimir_detalles()
print("")  # Salto de linea
capturar_datos()
empleado1.imprimir_detalles()
