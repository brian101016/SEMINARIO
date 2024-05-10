from django.contrib.auth.models import User


def user_a_usuario(user: User):
    """Convierte un 'user' en 'usuario', esto es, agregando el campo
    'permisos' según sea [admin, write, read] y además regresa un
    campo especial con el nombre extendido de dicho permiso ('permisos_name').

    Devuelve un Diccionario con los campos {id, username, email, is_superuser,
    permisos, permisos_name}.
    """

    usuario = {
        "id": user.pk,
        "username": user.username,
        "email": user.email,
        "is_superuser": user.is_superuser,
        "permisos": "none",
        "permisos_name": "Ninguno",
    }
    if "usuarios.admin" in user.get_user_permissions():
        usuario["permisos_name"] = "Administrador"
        usuario["permisos"] = "admin"

    elif "usuarios.write" in user.get_user_permissions():
        usuario["permisos_name"] = "Lectura y escritura"
        usuario["permisos"] = "write"

    elif "usuarios.read" in user.get_user_permissions():
        usuario["permisos_name"] = "Solo lectura"
        usuario["permisos"] = "read"

    # Si no existe el permiso, se toma 'none' y 'Ninguno' como permisos default.
    return usuario
