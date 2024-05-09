from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Bautizo
from .forms import (
    BuscarBautizoForm,
    BautizoForm,
    EliminarBautizoForm,
)


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

    return render(request, "bautizo/index.html", {"bautizos": bautizos, "form": form})


def crear_bautizo(request):
    form = BautizoForm()

    if request.method == "POST":
        form = BautizoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bautizos")

    return render(request, "bautizo/crear.html", {"form": form})


def editar_bautizo(request, id):
    bautizo = get_object_or_404(Bautizo, pk=id)
    form = BautizoForm(instance=bautizo)

    if request.method == "POST":
        form = BautizoForm(request.POST, instance=bautizo)

        if form.is_valid():
            form.save()
            return redirect("bautizos")

    return render(request, "bautizo/editar.html", {"form": form, "id": id})


def eliminar_bautizo(request, id):
    bautizo = get_object_or_404(Bautizo, id=id)
    form = EliminarBautizoForm(instance=bautizo)

    if request.method == "POST":
        bautizo.delete()
        return redirect("bautizos")

    return render(request, "bautizo/eliminar.html", {"form": form, "id": id})
