from django.contrib.auth.models import User


def user_a_usuario(user: User):
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

    return usuario
