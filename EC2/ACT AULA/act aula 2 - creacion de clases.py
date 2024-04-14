class Persona:
    def __init__(
        self,
        nombre: str,
        edad: int,
        genero: str,
        tipo_sangre: str,
        nacionalidad: str,
        color_ojos: str,
        palabra_favorita: str,
        esta_casado: bool,
    ):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self._tipo_sangre = tipo_sangre
        self._nacionalidad = nacionalidad
        self._color_ojos = color_ojos
        self._palabra_favorita = palabra_favorita
        self._esta_casado = esta_casado

    def __str__(self):
        return (
            f"\n**************\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Genero: {self.genero}"
        )

    def obtener_edad_en_dias(self):
        return self._edad * 365

    def obtener_edad_en_horas(self):
        return self.obtener_edad_en_dias() * 24

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if len(valor) == 0:
            raise ValueError
        else:
            self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor: int):
        if valor < 0:
            raise ValueError
        else:
            self._edad = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor: str):
        if valor == "Masculino" or valor == "Femenino" or valor == "No binario":
            self._genero = valor
        else:
            raise ValueError

    @property
    def tipo_sangre(self):
        return self._tipo_sangre

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, valor: str):
        if len(valor) == 0:
            raise ValueError
        else:
            self._nacionalidad = valor

    @property
    def color_ojos(self):
        return self._color_ojos

    @property
    def palabra_favorita(self):
        return self._palabra_favorita

    @palabra_favorita.setter
    def palabra_favorita(self, valor: str):
        if len(valor) == 0:
            raise ValueError
        else:
            self._palabra_favorita = valor

    @property
    def esta_casado(self):
        return self._esta_casado

    @esta_casado.setter
    def esta_casado(self, valor: bool):
        self._esta_casado = valor


# fin


# Funciones para llenar los campos mas rapido
def llenar_nombre():
    while True:
        try:
            persona1.nombre = input("Nombre: ")
            break
        except ValueError:
            print("Ingresa una cadena de texto valida")


def llenar_edad():
    while True:
        try:
            valor = int(input("Edad:"))
            persona1.edad = valor
            break
        except ValueError:
            print("Ingrese un valor numerico positivo!")


def llenar_genero():
    while True:
        try:
            persona1.genero = input("Genero:")
            break
        except ValueError:
            print(
                "Por favor ingresa un genero valido, las opciones son: Masculino, Femenino y No binario"
            )


# Lo creamos primero para despues modificarlo
persona1 = Persona("", -1, "", "O+", "", "", "", False)
print("Llenar valores:\n")

llenar_nombre()
llenar_edad()
llenar_genero()

print(persona1)
print(f"Edad en dias: {persona1.obtener_edad_en_dias()}")

print("\n### Modificar valores:\n")

llenar_nombre()
llenar_edad()
llenar_genero()

print(persona1)
print(f"Edad en dias: {persona1.obtener_edad_en_dias()}")
