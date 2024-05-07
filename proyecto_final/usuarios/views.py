from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.urls.base import reverse


from .forms import (
    BuscarUsuarioForm,
    CrearUsuarioForm,
    EditarUsuarioForm,
    EliminarUsuarioForm,
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
                usuarios = usuarios.filter(Q(user_permissions__codename=fil_permisos))

    format_usuarios = []
    for u in usuarios:
        format_usuarios.append(user_a_usuario(u))

    return render(
        request,
        "usuario/index.html",
        {"users": format_usuarios, "form": form},
    )


def crear_usuario(request):
    form = CrearUsuarioForm()

    if request.method == "POST":
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "usuario/crear.html", {"form": form})


def editar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    data = user_a_usuario(usuario)

    form = EditarUsuarioForm(data=data, instance=usuario)

    if request.method == "POST":
        form = EditarUsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "usuario/editar.html", {"form": form, "id": id})


def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    data = user_a_usuario(usuario)
    form = EliminarUsuarioForm(data=data, instance=usuario)

    if request.method == "POST":
        usuario.delete()
        return redirect("usuarios")

    return render(request, "usuario/eliminar.html", {"form": form, "id": id})
