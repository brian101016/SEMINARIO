class Empleado:
    # inicializador
    def __init__(self, nombre: str, edad: int, salario: float, departamento: str):
        # asignaremos los valores a los atributos
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento

    def __str__(self):
        return (
            f"Hola, soy {self.nombre} y tengo {self.edad} años"
            + f"Con un salario de ${self.salario}.00 en el departamento de {self.departamento}"
        )

    def saludar(self):
        print(f"Hola!, soy {self.nombre} y tengo {self.edad} años.")

    def mostrar_info(self):
        print("\nNombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Salario: ", self.salario)
        print("Departamento: ", self.departamento)


class Tecnico(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario, departamento)

    def reparar_equipo(self):
        self.salario += 5000
        print(f"\nEl salario de {self.nombre} ha aumentado a ${self.salario}")


# Instanciar
nuevo_tecnico = Tecnico(
    input("Ingresa el nombre: "),
    int(input("Ingresa la edad: ")),
    float(input("Ingresa el salario: ")),
    input("Ingresa el departamento: "),
)
nuevo_tecnico.saludar()
nuevo_tecnico.mostrar_info()
nuevo_tecnico.reparar_equipo()
