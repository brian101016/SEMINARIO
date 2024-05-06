from django.db import models


# Create your models here.
class GlobalPermissions(models.Model):

    class Meta:
        # No database table creation or deletion operations will be performed for this model.
        managed = False

        default_permissions = ()

        permissions = (
            ("read", "Solo lectura"),
            ("write", "Lectura y Escritura"),
            ("admin", "Administrador"),
        )
