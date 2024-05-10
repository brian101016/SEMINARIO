from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Bautizo
from .forms import (
    BuscarBautizoForm,
    BautizoForm,
    EliminarBautizoForm,
)


@login_required
def index(request):
    """Vista principal de 'Bautizos' con tabla de búsqueda."""

    # Creamos las variables con sus valores default.
    form = BuscarBautizoForm()
    bautizos = Bautizo.objects.all()

    if request.method == "POST":
        form = BuscarBautizoForm(request.POST)
        if form.is_valid():
            bautizos = aplicar_filtros(form.cleaned_data)  # Actualizamos la lista.

    return render(request, "bautizos/index.html", {"bautizos": bautizos, "form": form})


@permission_required("usuarios.write")
def crear_bautizo(request):
    """Vista para crear y guardar un bautizo usando su 'ModelForm'."""

    form = BautizoForm()

    if request.method == "POST":
        form = BautizoForm(request.POST)  # Regeneramos el formulario.

        if form.is_valid():
            form.save()
            return redirect("bautizos")

    return render(request, "bautizos/crear.html", {"form": form})


@permission_required("usuarios.write")
def editar_bautizo(request, id):
    """Vista para editar un registro (si existe su 'id')."""

    bautizo = get_object_or_404(Bautizo, pk=id)
    form = BautizoForm(instance=bautizo)

    if request.method == "POST":
        form = BautizoForm(request.POST, instance=bautizo)

        if form.is_valid():
            form.save()
            return redirect("bautizos")

    return render(request, "bautizos/editar.html", {"form": form, "id": id})


@permission_required("usuarios.write")
def eliminar_bautizo(request, id):
    """Vista de confirmación para eliminar un registro (si existe)."""

    bautizo = get_object_or_404(Bautizo, id=id)
    form = EliminarBautizoForm(instance=bautizo)

    # El método POST funciona como doble confirmación para eliminar
    if request.method == "POST":
        bautizo.delete()
        return redirect("bautizos")

    return render(request, "bautizos/eliminar.html", {"form": form, "id": id})


def aplicar_filtros(filtros):
    """Extraemos y aplicamos todos los filtros al modelo.

    El parámetro 'filtros' está pensado para extraerse desde 'form.cleaned_data'
    del formulario de búsqueda de un modelo específico (Bautizos).

    Se verifica por cualquier valor existente (not None) para aplicar una query
    de búsqueda utilizando '.filter()'.

    Los filtros que sean cadena se aplican según 'llave__icontains=valor'.
    Los filtros que sean fechas o números se filtran dentro de un rango definido
    según 'campo_min' y 'campo_max'.
    Los filtros que sean booleanos se aplican directamente como 'llave=valor'.
    """

    # Lista con todos los registros para irle agregando los filtros.
    todos = Bautizo.objects.all()

    nombre = filtros["nombre"]
    if nombre is not None:
        todos = todos.filter(nombre__icontains=nombre)

    sexo = filtros["sexo"]
    if sexo is not None:
        todos = todos.filter(sexo=sexo)

    fecha_nacimiento_min = filtros["fecha_nacimiento_min"]
    if fecha_nacimiento_min is not None:
        todos = todos.filter(fecha_nacimiento__gte=fecha_nacimiento_min)

    fecha_nacimiento_max = filtros["fecha_nacimiento_max"]
    if fecha_nacimiento_max is not None:
        todos = todos.filter(fecha_nacimiento__lte=fecha_nacimiento_max)

    ciudad_nacimiento = filtros["ciudad_nacimiento"]
    if ciudad_nacimiento is not None:
        todos = todos.filter(ciudad_nacimiento__icontains=ciudad_nacimiento)

    folio_acta_nacimiento = filtros["folio_acta_nacimiento"]
    if folio_acta_nacimiento is not None:
        todos = todos.filter(folio_acta_nacimiento__icontains=folio_acta_nacimiento)

    padre = filtros["padre"]
    if padre is not None:
        todos = todos.filter(padre__icontains=padre)

    madre = filtros["madre"]
    if madre is not None:
        todos = todos.filter(madre__icontains=madre)

    abuelos_paternos = filtros["abuelos_paternos"]
    if abuelos_paternos is not None:
        todos = todos.filter(abuelos_paternos__icontains=abuelos_paternos)

    abuelos_paternos = filtros["abuelos_paternos"]
    if abuelos_paternos is not None:
        todos = todos.filter(abuelos_paternos__icontains=abuelos_paternos)

    padrino = filtros["padrino"]
    if padrino is not None:
        todos = todos.filter(padrino__icontains=padrino)

    madrina = filtros["madrina"]
    if madrina is not None:
        todos = todos.filter(madrina__icontains=madrina)

    notas_marginales = filtros["notas_marginales"]
    if notas_marginales is not None:
        todos = todos.filter(notas_marginales__icontains=notas_marginales)

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

    return todos  # Ahora 'todos' es un query con la suma de filtros
