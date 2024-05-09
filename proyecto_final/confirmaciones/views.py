from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Confirmacion
from .forms import (
    BuscarConfirmacionForm,
    ConfirmacionForm,
    EliminarConfirmacionForm,
)


def index(request):
    form = BuscarConfirmacionForm()
    confirmaciones = Confirmacion.objects.all()

    if request.method == "POST":
        form = BuscarConfirmacionForm(request.POST)
        if form.is_valid():
            busqueda = ""
            confirmaciones = Confirmacion.objects.filter(
                Q(nombre__icontains=busqueda)
                | Q(padre__icontains=busqueda)
                | Q(madre__icontains=busqueda)
                | Q(parroquia_bautizo__icontains=busqueda)
            )
        # AQUI PONEMOS TODOS LOS CAMPOS

    return render(
        request,
        "confirmaciones/index.html",
        {"confirmaciones": confirmaciones, "form": form},
    )


def crear_confirmacion(request):
    form = ConfirmacionForm()

    if request.method == "POST":
        form = ConfirmacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirmaciones")

    return render(request, "confirmaciones/crear.html", {"form": form})


def editar_confirmacion(request, id):
    confirmacion = get_object_or_404(Confirmacion, pk=id)
    form = ConfirmacionForm(instance=confirmacion)

    if request.method == "POST":
        form = ConfirmacionForm(request.POST, instance=confirmacion)

        if form.is_valid():
            form.save()
            return redirect("confirmaciones")

    return render(request, "confirmaciones/editar.html", {"form": form, "id": id})


def eliminar_confirmacion(request, id):
    confirmacion = get_object_or_404(Confirmacion, id=id)
    form = EliminarConfirmacionForm(instance=confirmacion)

    if request.method == "POST":
        confirmacion.delete()
        return redirect("comuniones")

    return render(request, "confirmaciones/eliminar.html", {"form": form, "id": id})
