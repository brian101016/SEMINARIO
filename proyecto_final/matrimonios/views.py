from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Matrimonio
from .forms import (
    BuscarMatrimonioForm,
    MatrimonioForm,
    EliminarMatrimonioForm,
)


@login_required
def index(request):
    """Vista principal de 'Matrimonios' con tabla de búsqueda."""

    # Creamos las variables con sus valores default.
    form = BuscarMatrimonioForm()
    matrimonios = Matrimonio.objects.all()

    if request.method == "POST":
        form = BuscarMatrimonioForm(request.POST)

        if form.is_valid():
            matrimonios = aplicar_filtros(form.cleaned_data)  # Actualizamos la lista.

    return render(
        request, "matrimonios/index.html", {"matrimonios": matrimonios, "form": form}
    )


@permission_required("usuarios.write")
def crear_matrimonio(request):
    """Vista para crear y guardar un matrimonio usando su 'ModelForm'."""

    form = MatrimonioForm()

    if request.method == "POST":
        form = MatrimonioForm(request.POST)  # Regeneramos el formulario.

        if form.is_valid():
            form.save()
            return redirect("matrimonios")

    return render(request, "matrimonios/crear.html", {"form": form})


@permission_required("usuarios.write")
def editar_matrimonio(request, id):
    """Vista para editar un registro (si existe su 'id')."""

    matrimonio = get_object_or_404(Matrimonio, pk=id)
    form = MatrimonioForm(instance=matrimonio)

    if request.method == "POST":
        form = MatrimonioForm(request.POST, instance=matrimonio)

        if form.is_valid():
            form.save()
            return redirect("matrimonios")

    return render(request, "matrimonios/editar.html", {"form": form, "id": id})


@permission_required("usuarios.write")
def eliminar_matrimonio(request, id):
    """Vista de confirmación para eliminar un registro (si existe)."""

    matrimonio = get_object_or_404(Matrimonio, id=id)
    form = EliminarMatrimonioForm(instance=matrimonio)

    # El método POST funciona como doble confirmación para eliminar.
    if request.method == "POST":
        matrimonio.delete()
        return redirect("matrimonios")

    return render(request, "matrimonios/eliminar.html", {"form": form, "id": id})


def aplicar_filtros(filtros):
    """Extraemos y aplicamos todos los filtros al modelo.

    El parámetro 'filtros' está pensado para extraerse desde 'form.cleaned_data'
    del formulario de búsqueda de un modelo específico (Matrimonio).

    Se verifica por cualquier valor existente (not None) para aplicar una query
    de búsqueda utilizando '.filter()'.

    Los filtros que sean cadena se aplican según 'llave__icontains=valor'.
    Los filtros que sean fechas o números se filtran dentro de un rango definido
    según 'campo_min' y 'campo_max'.
    Los filtros que sean booleanos se aplican directamente como 'llave=valor'.
    """

    # Lista con todos los registros para irle agregando los filtros.
    todos = Matrimonio.objects.all()

    novio = filtros["novio"]
    if novio is not None:
        todos = todos.filter(novio__icontains=novio)

    novia = filtros["novia"]
    if novia is not None:
        todos = todos.filter(novia__icontains=novia)

    domicilio = filtros["domicilio"]
    if domicilio is not None:
        todos = todos.filter(domicilio__icontains=domicilio)

    ciudad_sacramento = filtros["ciudad_sacramento"]
    if ciudad_sacramento is not None:
        todos = todos.filter(ciudad_sacramento__icontains=ciudad_sacramento)

    padres_novio = filtros["padres_novio"]
    if padres_novio is not None:
        todos = todos.filter(padres_novio__icontains=padres_novio)

    padres_novia = filtros["padres_novia"]
    if padres_novia is not None:
        todos = todos.filter(padres_novia__icontains=padres_novia)

    testigos = filtros["testigos"]
    if testigos is not None:
        todos = todos.filter(testigos__icontains=testigos)

    presentacion = filtros["presentacion"]
    if presentacion is not None:
        todos = todos.filter(presentacion__icontains=presentacion)

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
        todos = todos.filter(libro__gte=libro_max)

    pagina_min = filtros["pagina_min"]
    if pagina_min is not None:
        todos = todos.filter(pagina__lte=pagina_min)

    pagina_max = filtros["pagina_max"]
    if pagina_max is not None:
        todos = todos.filter(pagina__gte=pagina_max)

    partida_min = filtros["partida_min"]
    if partida_min is not None:
        todos = todos.filter(partida__lte=partida_min)

    partida_max = filtros["partida_max"]
    if partida_max is not None:
        todos = todos.filter(partida__gte=partida_max)

    notas = filtros["notas"]
    if notas is not None:
        todos = todos.filter(notas__icontains=notas)

    return todos  # Ahora 'todos' es un query con la suma de filtros.
