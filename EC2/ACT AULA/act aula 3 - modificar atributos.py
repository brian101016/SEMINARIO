class Empleado:
    # def __init__(self):
    #   self.puesto = None
    #   self.nombre = nombre
    #   self.edad = edad
    #   self.salario = salario

    def actualizar_atributos(self, nombre, edad, sueldo):
        try:
            verificar = self.nombre # Esto es para verificar si existe o no el atributo
        except AttributeError:
            print("El atributo 'nombre' no existe.")

        print("Modificando el atributo 'nombre'.")
        self.nombre = nombre


        try:
            verificar = self.edad
        except AttributeError:
            print("El atributo 'edad' no existe.")

        print("Modificando el atributo 'edad'.")
        self.edad = edad


        try:
            verificar = self.sueldo
        except AttributeError:
            print("El atributo 'sueldo' no existe.")

        print("Modificando el atributo 'sueldo'.")
        self.sueldo = sueldo

    def mostrar_info(self):
        try:
            print(f"Nombre: {self.nombre}, Edad: {self.edad}, Suelo: {self.sueldo}")
        except AttributeError:
            print("No hay informacion suficiente!")


# Creamos al empleado sin atributos
per = Empleado()
per.mostrar_info()  # Mostramos, pero marcara error

per.actualizar_atributos("Ana", 28, 48000)
per.mostrar_info()  # Ahora si se ven

per.actualizar_atributos("Ana Gomez", 30, 50000)
per.mostrar_info()  # Ahora estan actualizados los atributos

try:
    verificar = per.puesto
except AttributeError:
    print("El atributo 'puesto' no existe.")
    print("Modificando el atributo 'puesto'.")
    per.puesto = "Analista"
    
print(f"Puesto de la persona: {per.puesto}")
