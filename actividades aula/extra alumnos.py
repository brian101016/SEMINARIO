# Crear uan lista: tuplas, elementos, diccionarios
alumnos = [
    # Diccionarios: {key: value, key: value}
    {"nombre": "Hector", "cal": [10.0, 9.5, 8.6, 7.6]},  # 9.3
    {"nombre": "Oscar", "cal": [9.76, 8.5, 7.6, 6.6]},  # 7.7, 8.9
    {"nombre": "Jesus", "cal": [8.76, 7.5, 6.6, 3.6]},  # 6.3, 3.6
]


def calcular_promedio(cal):
    total = sum(cal)
    promedio = total / len(cal)
    return promedio


def mejor(estudiantes):
    mejor_prom = 0
    mejor_est = None
    for alumno in estudiantes:
        prom = calcular_promedio(alumno["cal"])
        if prom > mejor_prom:
            mejor_prom = prom
            mejor_est = alumno["nombre"]
    return mejor_est


def agregar_cali(alumnos, nombre, calificaciones):
    for al in alumnos:
        if al["nombre"] == nombre:
            for cal in calificaciones:
                al["cal"].append(cal)
            print(al["cal"])


def mostrar_alumnos(alumnos):
    for alumno in alumnos:
        nombre = alumno["nombre"]
        calificaciones = alumno["cal"]
        promedio = calcular_promedio(calificaciones)
        print(
            f"Alumno: {nombre}, Calificaciones: {calficaciones}, Promedio: {promedio}"
        )
    print(f"Mejor estudiante: {mejor(alumnos)}")


mostrar_alumnos(alumnos)
agregar_cali(alumnos, "Hector", [9.3])
agregar_cali(alumnos, "Oscar", [7.7, 8.9])
agregar_cali(alumnos, "Jesus", [6.3, 3.6])
mostrar_alumnos(alumnos)
