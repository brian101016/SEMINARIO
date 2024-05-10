from django import forms
from django.contrib.auth.forms import UserCreationForm, password_validation
from django.contrib.auth.models import User, Permission
from django.core.exceptions import ValidationError


from .models import GlobalPermissions
from webapp.utils import ReadOnlyFormMixin


class BuscarUsuarioForm(forms.Form):

    PERMISSIONS_CHOICES = ((None, "Cualquiera"),) + GlobalPermissions._meta.permissions

    username = forms.CharField(required=False)
    email = forms.CharField(required=False)
    permisos = forms.ChoiceField(choices=PERMISSIONS_CHOICES, required=False)


class CrearUsuarioForm(UserCreationForm):

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
        permisos = self.cleaned_data["permisos"]

        if not Permission.objects.filter(codename=permisos).exists():
            raise ValidationError("El valor ingresado no existe", "no_permission")
        return permisos

    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data["email"]
        permisos = self.cleaned_data["permisos"]
        permiso_obj = Permission.objects.get(codename=permisos)
        user.user_permissions.set([permiso_obj.pk])

        if permisos == "admin":
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        if commit:
            user.save()

        return user


class EditarUsuarioForm(forms.ModelForm):
    USER_ACCESS = None

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.USER_ACCESS = user

    class Meta:
        model = User
        fields = ["username", "email"]

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
        permisos = self.cleaned_data["permisos"]
        user = self.instance
        if self.USER_ACCESS and self.USER_ACCESS.id == user.id and permisos != "admin":
            raise ValidationError(
                "No es posible desacreditarse como admin", "no_permission"
            )

        if not Permission.objects.filter(codename=permisos).exists():
            raise ValidationError("El valor ingresado no existe", "no_permission")
        return permisos

    def clean(self):
        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]

        if pass1 or pass2:
            password_validation.validate_password(pass1)
            password_validation.validate_password(pass2)

            if pass1 != pass2:
                error = ValidationError(
                    "La nueva contraseña no coincide", "password_error"
                )
                self.add_error("password2", error)

        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]

        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])

        permisos = self.cleaned_data["permisos"]
        permiso_obj = Permission.objects.get(codename=permisos)
        user.user_permissions.set([permiso_obj.pk])

        if permisos == "admin":
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        if commit:
            user.save()

        return user


class EliminarUsuarioForm(ReadOnlyFormMixin, EditarUsuarioForm):
    pass
