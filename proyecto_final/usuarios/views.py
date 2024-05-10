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


@permission_required("usuarios.admin", raise_exception=True)
def index(request):
    """Vista principal de 'Usuarios' con tabla de búsqueda."""

    # Creamos las variables con sus valores default.
    form = BuscarUsuarioForm()
    usuarios = User.objects.all()

    if request.method == "POST":
        form = BuscarUsuarioForm(request.POST)

        if form.is_valid():
            usuarios = aplicar_filtros(form.cleaned_data)  # Actualizamos la lista.

    # Procesamos los users para considerar el campo 'permisos'.
    usuarios_formato = []
    for u in usuarios:
        usuarios_formato.append(user_a_usuario(u))

    return render(
        request,
        "usuarios/index.html",
        {"usuarios": usuarios_formato, "form": form},
    )


@permission_required("usuarios.admin", raise_exception=True)
def crear_usuario(request):
    """Vista para crear y guardar un usuario usando su 'ModelForm'."""

    form = CrearUsuarioForm()

    if request.method == "POST":
        form = CrearUsuarioForm(request.POST)  # Regeneramos el formulario.

        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "usuarios/crear.html", {"form": form})


@permission_required("usuarios.admin", raise_exception=True)
def editar_usuario(request, id):
    """Vista para editar un usuario (si existe su 'id')."""

    usuario = get_object_or_404(User, pk=id)

    data = user_a_usuario(usuario)  # Consideramos el campo 'permisos'.
    form = EditarUsuarioForm(data=data, instance=usuario, user=request.user)

    if request.method == "POST":
        form = EditarUsuarioForm(request.POST, instance=usuario, user=request.user)

        if form.is_valid():
            form.save()
            return redirect("usuarios")

    return render(request, "usuarios/editar.html", {"form": form, "id": id})


@permission_required("usuarios.admin", raise_exception=True)
def eliminar_usuario(request, id):
    """Vista de confirmación para eliminar un usuario (si existe)."""

    usuario = get_object_or_404(User, pk=id)

    data = user_a_usuario(usuario)  # Consideramos el campo 'permisos'.
    form = EliminarUsuarioForm(data=data, instance=usuario)

    if request.method == "POST":

        # Evitamos que el usuario se elimine a sí mismo.
        if request.user.id != usuario.id:
            usuario.delete()

        return redirect("usuarios")

    return render(request, "usuarios/eliminar.html", {"form": form, "id": id})


def aplicar_filtros(filtros):
    """Extraemos y aplicamos todos los filtros al modelo.

    El parámetro 'filtros' está pensado para extraerse desde 'form.cleaned_data'
    del formulario de búsqueda de un modelo específico (User).

    Se verifica por cualquier valor existente (not None) para aplicar una query
    de búsqueda utilizando '.filter()'.

    Los filtros que sean cadena se aplican según 'llave__icontains=valor'.
    Los filtros que sean fechas o números se filtran dentro de un rango definido
    según 'campo_min' y 'campo_max'.
    Los filtros que sean booleanos se aplican directamente como 'llave=valor'.
    """

    # Lista con todos los usuarios para irle agregando los filtros.
    todos = User.objects.all()

    username = filtros["username"]
    if username is not None:
        usuarios = usuarios.filter(username__icontains=username)

    email = filtros["email"]
    if email is not None:
        usuarios = usuarios.filter(email__icontains=email)

    permisos = filtros["permisos"]
    if permisos:
        usuarios = usuarios.filter(Q(user_permissions__codename=permisos))

    return todos  # Ahora 'todos' es un query con la suma de filtros.
