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
    form = BuscarBautizoForm()
    bautizos = Bautizo.objects.all()

    if request.method == "POST":
        form = BuscarBautizoForm(request.POST)
        if form.is_valid():
            busqueda = ""
            bautizos = Bautizo.objects.filter(
                Q(nombre__icontains=busqueda)
                | Q(padre__icontains=busqueda)
                | Q(madre__icontains=busqueda)
            )
            # AQUI PONEMOS TODOS LOS CAMPOS

    return render(request, "bautizos/index.html", {"bautizos": bautizos, "form": form})


@permission_required("usuarios.write")
def crear_bautizo(request):
    form = BautizoForm()

    if request.method == "POST":
        form = BautizoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bautizos")

    return render(request, "bautizos/crear.html", {"form": form})


@permission_required("usuarios.write")
def editar_bautizo(request, id):
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
    bautizo = get_object_or_404(Bautizo, id=id)
    form = EliminarBautizoForm(instance=bautizo)

    if request.method == "POST":
        bautizo.delete()
        return redirect("bautizos")

    return render(request, "bautizos/eliminar.html", {"form": form, "id": id})
