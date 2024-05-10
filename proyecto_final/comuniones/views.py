from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Comunion
from .forms import (
    BuscarComunionForm,
    ComunionForm,
    EliminarComunionForm,
)


@login_required
def index(request):
    form = BuscarComunionForm()
    comuniones = Comunion.objects.all()

    if request.method == "POST":
        form = BuscarComunionForm(request.POST)
        if form.is_valid():
            comuniones = aplicar_filtros(form.cleaned_data)

    return render(
        request, "comuniones/index.html", {"comuniones": comuniones, "form": form}
    )


@permission_required("usuarios.write")
def crear_comunion(request):
    form = ComunionForm()

    if request.method == "POST":
        form = ComunionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comuniones")

    return render(request, "comuniones/crear.html", {"form": form})


@permission_required("usuarios.write")
def editar_comunion(request, id):
    comunion = get_object_or_404(Comunion, pk=id)
    form = ComunionForm(instance=comunion)

    if request.method == "POST":
        form = ComunionForm(request.POST, instance=comunion)

        if form.is_valid():
            form.save()
            return redirect("comuniones")

    return render(request, "comuniones/editar.html", {"form": form, "id": id})


@permission_required("usuarios.write")
def eliminar_comunion(request, id):
    comunion = get_object_or_404(Comunion, id=id)
    form = EliminarComunionForm(instance=comunion)

    if request.method == "POST":
        comunion.delete()
        return redirect("comuniones")

    return render(request, "comuniones/eliminar.html", {"form": form, "id": id})


def aplicar_filtros(filtros):
    todos = Comunion.objects.all()

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

    return todos
