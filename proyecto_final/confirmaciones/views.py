from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Confirmacion
from .forms import (
    BuscarConfirmacionForm,
    ConfirmacionForm,
    EliminarConfirmacionForm,
)


@login_required
def index(request):
    """Vista principal de 'Confirmaciones' con tabla de búsqueda."""

    # Creamos las variables con sus valores default.
    form = BuscarConfirmacionForm()
    confirmaciones = Confirmacion.objects.all()

    if request.method == "POST":
        form = BuscarConfirmacionForm(request.POST)

        if form.is_valid():
            # Actualizamos la lista.
            confirmaciones = aplicar_filtros(form.cleaned_data)

    return render(
        request,
        "confirmaciones/index.html",
        {"confirmaciones": confirmaciones, "form": form},
    )


@permission_required("usuarios.write")
def crear_confirmacion(request):
    """Vista para crear y guardar una confirmación usando su 'ModelForm'."""

    form = ConfirmacionForm()

    if request.method == "POST":
        form = ConfirmacionForm(request.POST)  # Regeneramos el formulario.

        if form.is_valid():
            form.save()
            return redirect("confirmaciones")

    return render(request, "confirmaciones/crear.html", {"form": form})


@permission_required("usuarios.write")
def editar_confirmacion(request, id):
    """Vista para editar un registro (si existe su 'id')."""

    confirmacion = get_object_or_404(Confirmacion, pk=id)
    form = ConfirmacionForm(instance=confirmacion)

    if request.method == "POST":
        form = ConfirmacionForm(request.POST, instance=confirmacion)

        if form.is_valid():
            form.save()
            return redirect("confirmaciones")

    return render(request, "confirmaciones/editar.html", {"form": form, "id": id})


@permission_required("usuarios.write")
def eliminar_confirmacion(request, id):
    """Vista de confirmación para eliminar un registro (si existe)."""

    confirmacion = get_object_or_404(Confirmacion, id=id)
    form = EliminarConfirmacionForm(instance=confirmacion)

    # El método POST funciona como doble confirmación para eliminar
    if request.method == "POST":
        confirmacion.delete()
        return redirect("comuniones")

    return render(request, "confirmaciones/eliminar.html", {"form": form, "id": id})


def aplicar_filtros(filtros):
    """Extraemos y aplicamos todos los filtros al modelo.

    El parámetro 'filtros' está pensado para extraerse desde 'form.cleaned_data'
    del formulario de búsqueda de un modelo específico (Confirmacion).

    Se verifica por cualquier valor existente (not None) para aplicar una query
    de búsqueda utilizando '.filter()'.

    Los filtros que sean cadena se aplican según 'llave__icontains=valor'.
    Los filtros que sean fechas o números se filtran dentro de un rango definido
    según 'campo_min' y 'campo_max'.
    Los filtros que sean booleanos se aplican directamente como 'llave=valor'.
    """

    # Lista con todos los registros para irle agregando los filtros.
    todos = Confirmacion.objects.all()

    nombre = filtros["nombre"]
    if nombre is not None:
        todos = todos.filter(nombre__icontains=nombre)

    sexo = filtros["sexo"]
    if sexo is not None:
        todos = todos.filter(sexo=sexo)

    padre = filtros["padre"]
    if padre is not None:
        todos = todos.filter(padre__icontains=padre)

    madre = filtros["madre"]
    if madre is not None:
        todos = todos.filter(madre__icontains=madre)

    padrino_madrina = filtros["padrino_madrina"]
    if padrino_madrina is not None:
        todos = todos.filter(padrino_madrina__icontains=padrino_madrina)

    ciudad_bautizo = filtros["ciudad_bautizo"]
    if ciudad_bautizo is not None:
        todos = todos.filter(ciudad_bautizo__icontains=ciudad_bautizo)

    parroquia_bautizo = filtros["parroquia_bautizo"]
    if parroquia_bautizo is not None:
        todos = todos.filter(parroquia_bautizo__icontains=parroquia_bautizo)

    fecha_bautizo_min = filtros["fecha_bautizo_min"]
    if fecha_bautizo_min is not None:
        todos = todos.filter(fecha_bautizo__gte=fecha_bautizo_min)

    fecha_bautizo_max = filtros["fecha_bautizo_max"]
    if fecha_bautizo_max is not None:
        todos = todos.filter(fecha_bautizo__lte=fecha_bautizo_max)

    fecha_sacramento_min = filtros["fecha_sacramento_min"]
    if fecha_sacramento_min is not None:
        todos = todos.filter(fecha_sacramento__gte=fecha_sacramento_min)

    fecha_sacramento_max = filtros["fecha_sacramento_max"]
    if fecha_sacramento_max is not None:
        todos = todos.filter(fecha_sacramento__lte=fecha_sacramento_max)

    presbitero = filtros["presbitero"]
    if presbitero is not None:
        todos = todos.filter(presbitero__icontains=presbitero)

    libro_min = filtros["libro_min"]
    if libro_min is not None:
        todos = todos.filter(libro__lte=libro_min)

    libro_max = filtros["libro_max"]
    if libro_max is not None:
        todos = todos.filter(libro__lte=libro_max)

    pagina_min = filtros["pagina_min"]
    if pagina_min is not None:
        todos = todos.filter(pagina__lte=pagina_min)

    pagina_max = filtros["pagina_max"]
    if pagina_max is not None:
        todos = todos.filter(pagina__lte=pagina_max)

    partida_min = filtros["partida_min"]
    if partida_min is not None:
        todos = todos.filter(partida__lte=partida_min)

    partida_max = filtros["partida_max"]
    if partida_max is not None:
        todos = todos.filter(partida__lte=partida_max)

    notas = filtros["notas"]
    if notas is not None:
        todos = todos.filter(notas__icontains=notas)

    return todos  # Ahora 'todos' es un query con la suma de filtros.
