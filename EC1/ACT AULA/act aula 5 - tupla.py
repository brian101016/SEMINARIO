alumnos = [
    {"nombre": "Primero", "calificaciones": [0, 1, 2, 3]},
    {"nombre": "Segundo", "calificaciones": [4, 5, 6, 7]},
    {"nombre": "Tercero", "calificaciones": [8, 9, 0, 1]},
    {"nombre": "Cuarto", "calificaciones": [5, 8, 3, 1]},
]


def calif_mas_alta(alumnos):
    estudiante_maximo = "Ninguno"
    calificacion_maxima = 0

    for alumno in alumnos:
        for calif in alumno["calificaciones"]:
            if calif > calificacion_maxima:
                calificacion_maxima = calif
                estudiante_maximo = alumno["nombre"]

    return (estudiante_maximo, calificacion_maxima)


resultado = calif_mas_alta(alumnos)
print(
    f"El estudiante con la calificacion mas alta es {resultado[0]} con {resultado[1]} punto(s)."
)
