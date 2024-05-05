from django.db import models


# Create your models here.
class GlobalPermissions(models.Model):

    class Meta:
        # No database table creation or deletion operations will be performed for this model.
        managed = False

        default_permissions = ()

        permissions = (
            ("admin", "Administrador"),
            ("write", "Lectura y Escritura"),
            ("read", "Solo lectura"),
        )
