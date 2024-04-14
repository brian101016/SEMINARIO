class Persona:
    def __init__(self, nombre, edad):
        self._nombre = "Nuevo nombre"
        self._edad = 1
        if nombre is not None:
            self.set_nombre(nombre)
        if edad is not None:
            self.set_edad(edad)

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        if validar_string(valor):
            self._nombre = valor
            return True
        else:
            return False

    def get_edad(self):
        return self._edad

    def set_edad(self, valor):
        if validar_edad(valor):
            self._edad = valor
            return True
        else:
            return False


class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self._salario = 0.1
        if salario is not None:
            self.set_salario(salario)

    def __str__(self):
        return (f"Nombre: {self.get_nombre()}, "
                f"Edad: {self.get_edad()}, "
                f"Salario: {self.get_salario()}")

    def get_salario(self):
        return self._salario

    def set_salario(self, valor):
        if validar_flotante(valor):
            self._salario = valor
            return True
        else:
            return False

    def imprimir_detalles(self):
        print(self)

    def capturar_datos(self):
        # CAPTURAR DATOS
        while True:
            if self.set_nombre(input("Nombre del empleado: ")):
                break

        while True:
            if self.set_edad(convertir_entero(input("Edad del empleado: "))):
                break

        while True:
            if self.set_salario(convertir_flotante(input("Salario del empleado: "))):
                break


class Departamento:
    def __init__(self):
        self._empleados: list[Empleado] = []

    def get_empleados(self):
        return self._empleados

    def crear_empleado(self):
        # Lo creamos vacio, pero se autocompleta con valores default
        nuevo_empleado = Empleado(None, None, None)

        # Ahora si rellenamos la informacion correctamente
        print("Creando nuevo empleado...")
        nuevo_empleado.capturar_datos()

        # Lo guardamos y listo
        self._empleados.append(nuevo_empleado)
        print("Se ha creado con exito!")

    def mostrar_empleados(self):
        contador = 0
        for item in self.get_empleados():
            contador += 1
            print(f"{contador}.- {item}")
        if contador == 0:
            print("No hay empleados!")

    def aumentar_salarios(self, porcentaje: float):
        if porcentaje <= 0:
            print("El porcentaje debe ser mayor a 0!")
            return

        for item in self.get_empleados():
            salario = item.get_salario()
            salario += (salario * porcentaje) / 100
            item.set_salario(salario)

        print("Salarios modificados!")

    def recortar_personal(self, margen: float):
        if margen <= 0:
            print("El margen debe ser mayor a 0!")
            return

        contador = 0
        while contador < len(self._empleados):
            empleado_actual = self._empleados[contador]
            if empleado_actual.get_salario() < margen:
                print(f"Por eliminar: '{empleado_actual}'")
                del self._empleados[contador]
                contador -= 1

            contador += 1

        print("Empleados recortados!")


def validar_string(valor):
    if isinstance(valor, str) and valor != "":
        return True
    else:
        print("Ingresa una cadena valida!")
        return False


def validar_edad(valor):
    if isinstance(valor, int) and 0 < valor:
        return True
    else:
        print("Ingresa un numero entero valido mayor a 0!")
        return False


def validar_flotante(valor):
    if isinstance(valor, float) and 0 < valor:
        return True
    else:
        print("Ingresa un numero mayor a 0!")
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


# Hace lo mismo que la funcion convertir_entero, pero con tipo flotante
def convertir_flotante(valor):
    try:
        resultado = float(valor)
        return resultado
    except ValueError:
        # Mensaje opcional
        # print("Error al convertir, marcando 0 como default")
        return 0.0  # Default a 0 cuando haya error


# VARIABLES GLOBALES
dept = Departamento()
for i in range(3):
    dept.crear_empleado()  # Guardamos 3 empleados para probar

# Pruebas
print("\nINICIAN LAS PRUEBAS\n")
dept.mostrar_empleados()

empleado = dept.get_empleados()[0]  # Tomamos al primer empleado
print(f"Cambiar salario del empleado '{empleado.get_nombre()}'")

while True:
    if empleado.set_salario(convertir_flotante(input("Nuevo salario del empleado: "))):
        break

dept.mostrar_empleados()

print("\nAumentar salarios en 10%:")
dept.aumentar_salarios(10)
dept.mostrar_empleados()

print("\nDespedir empleados con salario menor a 3000")
dept.recortar_personal(3000)
dept.mostrar_empleados()
