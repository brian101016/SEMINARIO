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
            busqueda = ""
            comuniones = Comunion.objects.filter(
                Q(nombre__icontains=busqueda)
                | Q(padre__icontains=busqueda)
                | Q(madre__icontains=busqueda)
                | Q(parroquia_bautizo__icontains=busqueda)
            )
            # AQUI PONEMOS TODOS LOS CAMPOS

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
