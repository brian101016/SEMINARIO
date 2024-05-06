from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, logout as logout_func
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


from .forms import (
    BuscarUsuarioForm,
    CrearUsuarioForm,
    ModificarUsuarioForm,
    ReadOnlyUsuarioForm,
)
from .parse import user_a_usuario


# Create your views here.
def usuarios(request):
    form = BuscarUsuarioForm()
    usuarios = User.objects.all()

    if request.method == "POST":
        form = BuscarUsuarioForm(request.POST)
        if form.is_valid():
            fil_username = form.cleaned_data["username"]
            if fil_username is not None:
                usuarios = usuarios.filter(username__icontains=fil_username)
            fil_email = form.cleaned_data["email"]
            if fil_email is not None:
                usuarios = usuarios.filter(email__icontains=fil_email)
            fil_permisos = form.cleaned_data["permisos"]
            if fil_permisos:
                usuarios = usuarios.filter(
                    Q(user_permissions__codename=fil_permisos) | Q(is_superuser=True)
                )

    format_usuarios = []
    for u in usuarios:
        format_usuarios.append(user_a_usuario(u))

    return render(
        request,
        "registration/index.html",
        {"users": format_usuarios, "form": form},
    )


def nuevo_usuario(request):
    form = CrearUsuarioForm()

    if request.method == "POST":
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "registration/user_create.html", {"form": form})


def editar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    data = user_a_usuario(usuario)

    form = ModificarUsuarioForm(data=data, instance=usuario)

    if request.method == "POST":
        form = ModificarUsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "registration/user_edit.html", {"form": form, "id": id})


def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    data = user_a_usuario(usuario)
    form = ReadOnlyUsuarioForm(data=data, instance=usuario)

    if request.method == "POST":
        usuario.delete()
        return redirect("usuarios")

    return render(request, "registration/user_delete.html", {"form": form, "id": id})
