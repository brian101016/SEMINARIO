# -------------------------------- CLASE PERSONA
# QUE GUARDE INFORMACION DE SU NOMBRE, EDAD Y GENERO
class Persona:
    # -------------------------------- METODO INICIALIZADOR
    # MARCAMOS LOS PARAMETROS COMO OPCIONALES PARA CONSIDERAR DEFAULT
    def __init__(
            self,
            nombre: str | None = None,
            edad: int | None = None,
            genero: int | None = None
    ):
        # DECLARAMOS VALORES POR DEFECTO DE LA PERSONA,
        # ESTO GARANTIZA LA INTEGRIDAD DE LA INFORMACION
        self.__nombre = "Nueva persona"
        self.__edad = 1
        self.__genero = 2  # REPRESENTA AL GENERO 'OTRO'

        # EN CASO QUE EXISTAN PARAMETROS, LOS USAREMOS
        # RECORDEMOS QUE LAS FUNCIONES MANEJAN LOS ERRORES
        if nombre is not None:
            self.set_nombre(nombre)

        if edad is not None:
            self.set_edad(edad)

        if genero is not None:
            self.set_genero(genero)

    # -------------------------------- METODO PARA MOSTRAR COMO CADENA
    def __str__(self):
        return (f"Nombre: {self.get_nombre()}"
                f"\nEdad: {self.get_edad()}"
                f"\nGenero: {self.get_genero()}")

    # -------------------------------- FUNCIONES GET
    # SIMPLEMENTE PARA REGRESAR EL VALOR PROTEGIDO RESPECTIVAMENTE
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_genero(self):
        try:
            # EN CASO DE QUE SE MOFIQUEN LOS GENEROS, COMPROBAMOS
            return generos[self.__genero]
        except IndexError:
            self.__genero = 0  # CORREGIMOS
            return "Error!"  # INFORMAMOS DE UN ERROR

    # -------------------------------- FUNCIONES SET
    # AYUDAN A VERIFICAR LOS TIPOS DE DATOS Y RESTRICCIONES
    def set_nombre(self, valor: str):
        if string_valido(valor) is not None:
            self.__nombre = valor

    def set_edad(self, valor: int):
        if entero_valido(valor, True) is not None:
            self.__edad = valor

    def set_genero(self, valor: int):
        if indice_valido(valor, len(generos)) is not None:
            self.__genero = valor


# -------------------------------- FUNCIONES DE COMPROBACION DE TIPOS
# REVISA SI EL STRING ES VALIDO Y LO REGRESA, SINO REGRESA None
def string_valido(valor) -> str | None:
    if not isinstance(valor, str) or valor == "":
        print("--- Ingrese una cadena de texto valida!\n")
        return None
    return valor  # ESTE VALOR ES VALIDO


# REVISA SI EL ENTERO ES VALIDO Y LO REGRESA, SINO REGRESA None,
# TAMBIEN NOS PERMITE INDICAR SI QUEREMOS QUE SEA POSITIVO
def entero_valido(valor, es_positivo: bool) -> int | None:
    if not isinstance(valor, int) or (es_positivo and valor <= 0):
        if es_positivo:
            print("--- Ingrese un numero entero mayor a 0!\n")
        else:
            print("--- Ingrese un numero entero!\n")
        return None
    return valor  # ESTE VALOR ES VALIDO


# REVISA SI UN NUMERO REPRESENTA UN INDEX DE UNA LISTA
# EL PARAMETRO tamanio_maximo REPRESENTA EL len(lista)
def indice_valido(valor, tamanio_maximo: int) -> int | None:
    # EN CASO DE QUE LA LISTA ESTE VACIA, REGRESAMOS -1
    if tamanio_maximo == 0:
        print("--- Esta vacio!\n")
        return -1  # GRACIAS AL RESTO DE VERIFICACIONES, ESTO PREVIENE ERRORES

    # VERIFICAMOS SI EL NUMERO ES VALIDO PRIMERO,
    # SUMAMOS 1 EN CASO DE QUE SEA 0, PARA TOMARLO COMO VALIDO
    if entero_valido(valor + 1, True) is None:
        return None  # SIGNIFICA QUE EL NUMERO NO ERA VALIDO

    # DESPUES, VERIFICAMOS SI EL NUMERO ENTRA DENTRO DEL RANGO VALIDO,
    if not (tamanio_maximo > valor >= 0):
        print("--- Ingrese un numero valido de la lista!\n")
        return None  # NO EXISTE EN LA LISTA

    return valor  # ESTE VALOR ES VALIDO


# -------------------------------- FUNCIONES DE LECTURA RAPIDA
# FUNCION PARA OBTENER UNA CADENA DE TEXTO VALIDA 100%
def leer_string(mensaje: str) -> str:
    # CREAMOS UN CICLO 'INFINITO' PARA INSISTIR CON LA CAPTURA
    while True:
        try:
            # SOLICITAMOS EL VALOR Y LO COMPROBAMOS
            valor = string_valido(input(mensaje))

            # SI LA COMPROBACION FUNCIONA, REGRESAMOS EL VALOR
            if valor is not None:
                return valor  # CIERRA EL CICLO CON UN VALOR CORRECTO

            # NO ES NECESARIO MOSTRAR ERRORES GRACIAS A string_valido
            # continue
        except ValueError:
            # 'ATRAPAMOS' CUALQUIER ERROR INESPERADO Y REINICIAMOS EL CICLO
            print("--- Ingrese una cadena de texto valida!\n")


# FUNCION PARA OBTENER UN NUMERO ENTERO VALIDO 100%,
# PUDIENDO DECIR SI QUEREMOS QUE SEA POSITIVO O NO
def leer_entero(mensaje: str, es_positivo: bool) -> int:
    # CREAMOS UN CICLO 'INFINITO' PARA INSISTIR CON LA CAPTURA
    while True:
        try:
            # SOLICITAMOS EL VALOR, LO CONVERTIMOS A int Y LO COMPROBAMOS
            valor = entero_valido(int(input(mensaje)), es_positivo)

            # SI LA COMPROBACION FUNCIONA, REGRESAMOS EL VALOR
            if valor is not None:
                return valor  # CIERRA EL CICLO CON UN VALOR CORRECTO

            # NO ES NECESARIO MOSTRAR ERRORES GRACIAS A entero_valido
            # continue
        except ValueError:
            # 'ATRAPAMOS' CUALQUIER ERROR INESPERADO Y REINICIAMOS EL CICLO
            print("--- Ingrese un numero valido!\n")


# FUNCION PARA ESCOGER ENTRE UNA LISTA DE OPCIONES (Y TAMBIEN MUESTRA LAS OPCIONES)
def seleccionar_indice(mensaje: str, lista: list) -> int:
    # EN CASO DE QUE LA LISTA ESTE VACIA, REGRESAMOS -1
    if len(lista) == 0:
        print("--- Esta vacio!\n")
        return -1  # GRACIAS AL RESTO DE VERIFICACIONES, ESTO PREVIENE ERRORES

    # CREAMOS UN CICLO 'INFINITO' PARA INSISTIR CON LA CAPTURA
    while True:
        try:
            # PRIMERO MOSTRAMOS LAS OPCIONES
            print("Escriba el numero de la opcion que desee:")
            mostrar_lista(lista)  # USAMOS mostrar_lista

            # DESPUES SOLICITAMOS EL VALOR Y LO VERIFICAMOS
            # COMO LA LISTA COMIENZA EN 1, RESTAMOS PARA INCLUIR EL INDICE 0
            valor = indice_valido(int(input(mensaje)) - 1, len(lista))

            # SI LA COMPROBACION FUNCIONA, REGRESAMOS EL VALOR
            if valor is not None:
                return valor  # CIERRA EL CICLO CON UN VALOR CORRECTO

            # NO ES NECESARIO MOSTRAR ERRORES GRACIAS A indice_valido
            # continue
        except ValueError:
            # 'ATRAPAMOS' CUALQUIER ERROR INESPERADO Y REINICIAMOS EL CICLO
            print("--- Ingrese un numero valido de la lista!\n")


# FUNCION PARA MOSTRAR UNA LISTA JUNTO A SUS INDICES
def mostrar_lista(lista: list):
    indice = 0  # CREAMOS UN CONTADOR
    for item in lista:
        # MOSTRAMOS EL INDICE Y EL VALOR
        # EL INDICE SUMA 1 PARA CONTAR CON NUMEROS NATURALES
        print(f"   {indice + 1}. {item}")
        indice += 1  # AVANZAMOS

    # SI EL INDICE NUNCA CAMBIA, ES QUE NO HAY ITEMS EN LA LISTA
    if indice == 0:
        print("   Esta vacio!")
    print("")  # SALTO DE LINEA


# -------------------------------- COMENZAR EL PROGRAMA
print("=== ACTIVIDAD 6 - ENCAPSULAMIENTO ===\n")
# INICIALIZAMOS LA LISTA DE GENEROS VALIDOS COMO GLOBAL
generos = ["Masculino", "Femenino", "Otro"]

# CREAR A persona1 JUAN, 30 Y MASCULINO
persona1 = Persona("JUAN", 30, 0)

# IMPRIMIMOS LA PERSONA POR DEFECTO
# RECORDEMOS QUE EL METODO __str__ UTILIZA GET
print(persona1)
print("")  # SALTO DE LINEA

# MODIFICAR A persona1 PARA MARIA, 25 Y FEMENINO
# SOLICITAMOS AL USUARIO PARA MODIFICAR LOS DATOS
persona1.set_nombre(leer_string("Ingrese un nuevo nombre: "))
persona1.set_edad(leer_entero("Ingrese una nueva edad: ", True))
# UTILIZANDO LA FUNCION seleccionar_indice PODEMOS ESCOGER EL GENERO FACILMENTE
persona1.set_genero(seleccionar_indice("Ingrese un nuevo genero: ", generos))

# IMPRIMIMOS NUEVAMENTE A LA persona1 PARA MOSTRAR LOS CAMBIOS
print("\nDatos modificados:\n")
print(persona1)
