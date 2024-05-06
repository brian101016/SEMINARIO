from django import forms
from django.contrib.auth.forms import (
    UsernameField,
    UserCreationForm,
    password_validation,
)
from django.contrib.auth.models import UnicodeUsernameValidator, User, Permission
from django.core.exceptions import ValidationError

from .models import GlobalPermissions


class ReadOnlyFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReadOnlyFormMixin, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs["readonly"] = True
            self.fields[key].disabled = True

    def save(self, *args, **kwargs):
        # do not do anything
        pass


class BuscarUsuarioForm(forms.Form):
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
    permisos = forms.ChoiceField(choices=PERMISSIONS_CHOICES, required=False)
    is_active = forms.NullBooleanField(widget=YES_NO, required=False)
    is_staff = forms.NullBooleanField(widget=YES_NO, required=False)
    is_superuser = forms.NullBooleanField(widget=YES_NO, required=False)


class CrearUsuarioForm(UserCreationForm):

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
        else:
            user.is_superuser = False

        if commit:
            user.save()

        return user


class ModificarUsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email"]

    email = forms.EmailField(max_length=255, required=True, label="Correo electrónico")
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
        required=True,
        label="Permisos de usuario",
    )

    def clean_permisos(self):
        permisos = self.cleaned_data["permisos"]
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
        else:
            user.is_superuser = False

        if commit:
            user.save()

        return user


class ReadOnlyUsuarioForm(ReadOnlyFormMixin, ModificarUsuarioForm):
    pass
