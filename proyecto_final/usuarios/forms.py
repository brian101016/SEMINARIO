from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation


class UsuariosForm(forms.Form):
    PERMISSIONS_CHOICES = (
        (None, "Cualquiera"),
        ("SUPER", "Administrador"),
        ("WRITE", "Lectura y Escritura"),
        ("READ", "Solo lectura"),
    )

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
