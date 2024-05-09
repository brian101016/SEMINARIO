from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .forms import (
    BuscarUsuarioForm,
    CrearUsuarioForm,
    EditarUsuarioForm,
    EliminarUsuarioForm,
)
from .parse import user_a_usuario


def index(request):
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

    usuarios_formato = []
    for u in usuarios:
        usuarios_formato.append(user_a_usuario(u))

    return render(
        request,
        "usuarios/index.html",
        {"usuarios": usuarios_formato, "form": form},
    )


def crear_usuario(request):
    form = CrearUsuarioForm()

    if request.method == "POST":
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "usuarios/crear.html", {"form": form})


def editar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    data = user_a_usuario(usuario)

    form = EditarUsuarioForm(data=data, instance=usuario, user=request.user)

    if request.method == "POST":
        form = EditarUsuarioForm(request.POST, instance=usuario, user=request.user)

        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "usuarios/editar.html", {"form": form, "id": id})


def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    data = user_a_usuario(usuario)
    form = EliminarUsuarioForm(data=data, instance=usuario)

    if request.method == "POST":
        if request.user.id != usuario.id:
            usuario.delete()
        return redirect("usuarios")

    return render(request, "usuarios/eliminar.html", {"form": form, "id": id})
