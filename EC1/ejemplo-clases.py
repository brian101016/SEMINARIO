class Persona:
    # inicializador
    def __init__(self, nombre, edad, telefono, c_trabajo, c_vivienda):
        # asignaremos los valores a los atributos
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.c_trabajo = c_trabajo
        self.c_vivienda = c_vivienda

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.telefono}, {self.c_trabajo}, {self.c_vivienda}"

    def saludar(self):
        print(f"{self.nombre}, este es un saludo")


class Profesor(Persona):

    def __init__(self, nombre, edad, telefono, c_trabajo, c_vivienda, tipo_actividad):
        super().__init__(nombre, edad, telefono, c_trabajo, c_vivienda)
        self.tipo_actividad = tipo_actividad


# Instanciara
nueva_persona = Persona("Nuevo", 10, "1234567890", "Trabajo", "Vivienda")
nueva_persona.saludar()
print(nueva_persona)
