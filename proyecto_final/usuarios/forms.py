from django import forms
from django.contrib.auth.forms import UsernameField

from .models import GlobalPermissions


class BuscarUsuariosForm(forms.Form):
    PERMISSIONS_CHOICES = ((None, "Cualquiera"),) + GlobalPermissions._meta.permissions

    YES_NO = forms.Select(
        choices=[
            (None, "Cualquiera"),
            (True, "Si"),
            (False, "No"),
        ]
    )

    username = forms.CharField(max_length=255, required=False, empty_value=None)
    email = forms.CharField(max_length=255, required=False, empty_value=None)
    user_permissions = forms.ChoiceField(choices=PERMISSIONS_CHOICES, required=False)
    is_active = forms.NullBooleanField(widget=YES_NO, required=False)
    is_staff = forms.NullBooleanField(widget=YES_NO, required=False)
    is_superuser = forms.NullBooleanField(widget=YES_NO, required=False)


class NuevoUsuarioForm(forms.Form):

    nombre = UsernameField(max_length=24, required=True, label="Nombre de usuario")
    password1 = forms.CharField(
        max_length=32, required=True, widget=forms.PasswordInput, label="Contraseña"
    )
    password2 = forms.CharField(
        max_length=32,
        required=True,
        widget=forms.PasswordInput,
        label="Confirmar contraseña",
    )
    email = forms.EmailField(max_length=255, required=True, label="Correo electrónico")
    permisos = forms.ChoiceField(
        choices=GlobalPermissions._meta.permissions,
        required=True,
        label="Permisos de usuario",
    )
