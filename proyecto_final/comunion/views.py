from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Comunion
from .forms import (
    BuscarComunionForm,
    ComunionForm,
    EliminarComunionForm,
)


def comuniones(request):
    form = BuscarComunionForm()
    lista_comuniones = Comunion.objects.all()

    if request.method == "POST":
        form = BuscarComunionForm(request.POST)
        if form.is_valid():
            busqueda = ""
            lista_comuniones = Comunion.objects.filter(
                Q(nombre__icontains=busqueda)
                | Q(padre__icontains=busqueda)
                | Q(madre__icontains=busqueda)
                | Q(parroquia_bautizo__icontains=busqueda)
            )
            # AQUI PONEMOS TODOS LOS CAMPOS

    return render(
        request, "comunion/index.html", {"comuniones": lista_comuniones, "form": form}
    )


def crear_comunion(request):
    form = ComunionForm()

    if request.method == "POST":
        form = ComunionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comuniones")

    return render(request, "comunion/crear.html", {"form": form})


def editar_comunion(request, id):
    comunion = get_object_or_404(Comunion, pk=id)
    dd = comunion.fecha_bautizo
    print(dd)
    form = ComunionForm(instance=comunion)

    if request.method == "POST":
        form = ComunionForm(request.POST, instance=comunion)

        if form.is_valid():
            form.save()
            return redirect("comuniones")

    return render(request, "comunion/editar.html", {"form": form, "id": id})


def eliminar_comunion(request, id):
    comunion = get_object_or_404(Comunion, id=id)
    form = EliminarComunionForm(instance=comunion)

    if request.method == "POST":
        comunion.delete()
        return redirect("comuniones")

    return render(request, "comunion/eliminar.html", {"form": form, "id": id})
