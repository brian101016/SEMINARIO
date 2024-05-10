from django import forms
from django.contrib.auth.forms import UserCreationForm, password_validation
from django.contrib.auth.models import User, Permission
from django.core.exceptions import ValidationError


from .models import GlobalPermissions
from webapp.utils import ReadOnlyFormMixin


class BuscarUsuarioForm(forms.Form):
    """Campos específicos para buscar 'Users'.

    Este formulario también contempla el campo 'permisos'.
    """

    # Agregamos la opción None a los permisos globales.
    PERMISSIONS_CHOICES = ((None, "Cualquiera"),) + GlobalPermissions._meta.permissions

    username = forms.CharField(required=False)
    email = forms.CharField(required=False)
    permisos = forms.ChoiceField(choices=PERMISSIONS_CHOICES, required=False)


class CrearUsuarioForm(UserCreationForm):
    """Contiene campos y validaciones para crear 'Users'.

    Extiende de 'UserCreationForm' para utilizar las validaciones
    por defecto junto a sus campos.
    """

    # Sobreescribimos los campos autogenerados para considerar otras validaciones.
    password1 = forms.CharField(
        max_length=32, widget=forms.PasswordInput, label="Contraseña"
    )
    password2 = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput,
        label="Confirmar contraseña",
    )
    email = forms.EmailField(max_length=255, label="Correo electrónico")
    permisos = forms.ChoiceField(
        choices=GlobalPermissions._meta.permissions,
        label="Permisos de usuario",
    )

    def clean_permisos(self):
        """Validación personalizada de permisos existentes."""

        permisos = self.cleaned_data["permisos"]

        if not Permission.objects.filter(codename=permisos).exists():
            raise ValidationError("El valor ingresado no existe", "no_permission")

        return permisos  # Es válido.

    def save(self, commit=True):
        """Método para guardar el usuario con los campos personalizados.

        El formulario 'UserCreationForm' no considera al email ni otros campos,
        por lo que se agregan manualmente.

        Consideramos los permisos globales para ingresárselos al usuario,
        y además modificar 'is_staff' & 'is_superuser' respectivamente.
        """

        user = super().save(commit=True)  # Guardamos el usuario inicialmente.

        # Agregamos manualmente los campos al usuario.
        user.email = self.cleaned_data["email"]
        permisos = self.cleaned_data["permisos"]
        permiso_obj = Permission.objects.get(codename=permisos)
        user.user_permissions.set([permiso_obj.pk])

        # Marcamos superuser para acceder a página de admin.
        if permisos == "admin":
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        if commit:
            user.save()  # Guardamos el registro.

        return user


class EditarUsuarioForm(forms.ModelForm):
    """Contiene campos y validaciones para editar 'Users'.

    Similar a 'CrearUsuarioForm', pero permitiendo modificar
    la contraseña del usuario si así se desea.

    Además cuenta con verificaciones para evitar que un usuario
    se elimine así mismo (para poder seguir accediendo al sistema).
    """

    # Variable auxiliar que guarda el usuario que accede.
    USER_ACCESS = None

    def __init__(self, *args, user=None, **kwargs):
        """Contructor normal que además acepta un 'user' como kwarg."""

        super().__init__(*args, **kwargs)
        if user is not None:
            self.USER_ACCESS = user  # Sacamos al usuario del contructor.

    class Meta:
        """Vinculamos el formulario con el modelo de usuario."""

        model = User
        fields = ["username", "email"]

    # Sobreescribimos los campos autogenerados para considerar otras validaciones.
    email = forms.EmailField(max_length=255, label="Correo electrónico")
    password1 = forms.CharField(
        max_length=32,
        required=False,
        widget=forms.PasswordInput,
        label="Cambiar contraseña (opcional)",
    )
    password2 = forms.CharField(
        max_length=32,
        required=False,
        widget=forms.PasswordInput,
        label="Confirmar contraseña (solo para cambio)",
    )
    permisos = forms.ChoiceField(
        choices=GlobalPermissions._meta.permissions,
        label="Permisos de usuario",
    )

    def clean_permisos(self):
        """Validación personalizada de permisos existentes."""

        permisos = self.cleaned_data["permisos"]
        user = self.instance

        # Evitamos que el admin se quite a sí mismo los permisos.
        if self.USER_ACCESS and self.USER_ACCESS.id == user.id and permisos != "admin":
            raise ValidationError(
                "No es posible desacreditarse como admin", "no_permission"
            )

        # Validación similar a 'CrearUsuarioForm'.
        if not Permission.objects.filter(codename=permisos).exists():
            raise ValidationError("El valor ingresado no existe", "no_permission")

        return permisos

    def clean(self):
        """Simulamos la verificación de contraseñas de 'UserCreationForm'.

        Si no hay contraseñas a validar, se continúa con el flujo.
        """

        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]

        if pass1 or pass2:
            # Validación automática de Django.
            password_validation.validate_password(pass1)
            password_validation.validate_password(pass2)

            if pass1 != pass2:
                error = ValidationError(
                    "La nueva contraseña no coincide", "password_error"
                )
                self.add_error("password2", error)

        return super().clean()

    def save(self, commit=True):
        """Método para guardar el usuario con los campos personalizados.

        El formulario 'UserCreationForm' no considera al email ni otros campos,
        por lo que se agregan manualmente.

        Consideramos los permisos globales para ingresárselos al usuario,
        y además modificar 'is_staff' & 'is_superuser' respectivamente.
        """

        user = super().save(commit=False)  # Guardamos el usuario inicialmente.

        # Agregamos manualmente los campos al usuario.
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]

        # Verificamos si el usuario quiere modificar la contraseña.
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])

        permisos = self.cleaned_data["permisos"]
        permiso_obj = Permission.objects.get(codename=permisos)
        user.user_permissions.set([permiso_obj.pk])

        # Marcamos superuser para acceder a página de admin.
        if permisos == "admin":
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        if commit:
            user.save()  # Guardamos el registro.

        return user


class EliminarUsuarioForm(ReadOnlyFormMixin, EditarUsuarioForm):
    """Posee todos los campos desactivados para confirmar los datos."""

    pass
