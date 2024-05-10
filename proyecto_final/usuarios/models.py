from django.db import models


class GlobalPermissions(models.Model):
    """Información auxiliar para registrar permisos globales."""

    class Meta:
        managed = False  # Evitamos crear tablas y operaciones de BD.

        # Sobreescribimos los permisos default y marcamos nuevos.
        default_permissions = ()
        permissions = (
            ("read", "Solo lectura"),
            ("write", "Lectura y Escritura"),
            ("admin", "Administrador"),
        )
