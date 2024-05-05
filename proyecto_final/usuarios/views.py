# from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_func
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required


from .forms import BuscarUsuariosForm, NuevoUsuarioForm


# Create your views here.
def usuarios(request):
    buscar_usuarios = BuscarUsuariosForm()
    usuarios = User.objects.all()

    if request.method == "POST":
        buscar_usuarios = BuscarUsuariosForm(request.POST)
        if buscar_usuarios.is_valid():
            fil_username = buscar_usuarios.cleaned_data["username"]
            if fil_username is not None:
                usuarios = usuarios.filter(username__icontains=fil_username)
            fil_email = buscar_usuarios.cleaned_data["email"]
            if fil_email is not None:
                usuarios = usuarios.filter(email__icontains=fil_email)
            # fil_user_permissions = buscar_usuarios.cleaned_data["user_permissions"]
            # if fil_user_permissions is not None:
            #     usuarios = usuarios.filter( user_permissions=fil_user_permissions )
            fil_is_active = buscar_usuarios.cleaned_data["is_active"]
            if fil_is_active is not None:
                usuarios = usuarios.filter(is_active=fil_is_active)
            fil_is_staff = buscar_usuarios.cleaned_data["is_staff"]
            if fil_is_staff is not None:
                usuarios = usuarios.filter(is_staff=fil_is_staff)
            fil_is_superuser = buscar_usuarios.cleaned_data["is_superuser"]
            if fil_is_superuser is not None:
                usuarios = usuarios.filter(is_superuser=fil_is_superuser)

    return render(
        request,
        "registration/index.html",
        {"users": usuarios, "buscar_usuarios": buscar_usuarios},
    )


def nuevo_usuario(request):
    nuevo_usuario_form = NuevoUsuarioForm()

    if request.method == "POST":
        nuevo_usuario_form = NuevoUsuarioForm(request.POST)
        if nuevo_usuario_form.is_valid():
            print(f"Is valid: {nuevo_usuario_form.cleaned_data}")
            nombre = nuevo_usuario_form.cleaned_data["nombre"]
            password1 = nuevo_usuario_form.cleaned_data["password1"]
            password2 = nuevo_usuario_form.cleaned_data["password2"]
            email = nuevo_usuario_form.cleaned_data["email"]
            permisos = nuevo_usuario_form.cleaned_data["permisos"]

            if password1 == password2:
                usuario = User.objects.create(
                    username=nombre,
                    password=password1,
                    email=email,
                )

                usuario.user_permissions.add(f"usuarios.{permisos}")

                if permisos == "admin":
                    usuario.is_superuser = True

                usuario.save()
                print(f"SUCCESS: {usuario}")
                return redirect("usuarios")
            else:
                nuevo_usuario_form.add_error(
                    "password2", "Las contraseñas no coinciden"
                )
        else:
            print(f"Is not valid, {nuevo_usuario_form.error_messages}")

    return render(
        request, "registration/user_create.html", {"form": nuevo_usuario_form}
    )
