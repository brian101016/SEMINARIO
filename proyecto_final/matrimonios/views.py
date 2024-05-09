from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from .models import Matrimonio
from .forms import (
    BuscarMatrimonioForm,
    MatrimonioForm,
    EliminarMatrimonioForm,
)


def index(request):
    form = BuscarMatrimonioForm()
    matrimonios = Matrimonio.objects.all()

    if request.method == "POST":
        form = BuscarMatrimonioForm(request.POST)
        if form.is_valid():
            busqueda = ""
            matrimonios = Matrimonio.objects.filter(
                Q(novio__icontains=busqueda) | Q(novia__icontains=busqueda)
            )
            # AQUI PONEMOS TODOS LOS CAMPOS

    return render(
        request, "matrimonios/index.html", {"matrimonios": matrimonios, "form": form}
    )


def crear_matrimonio(request):
    form = MatrimonioForm()

    if request.method == "POST":
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("matrimonios")

    return render(request, "matrimonios/crear.html", {"form": form})


def editar_matrimonio(request, id):
    matrimonio = get_object_or_404(Matrimonio, pk=id)
    form = MatrimonioForm(instance=matrimonio)

    if request.method == "POST":
        form = MatrimonioForm(request.POST, instance=matrimonio)

        if form.is_valid():
            form.save()
            return redirect("matrimonios")

    return render(request, "matrimonios/editar.html", {"form": form, "id": id})


def eliminar_matrimonio(request, id):
    matrimonio = get_object_or_404(Matrimonio, id=id)
    form = EliminarMatrimonioForm(instance=matrimonio)

    if request.method == "POST":
        matrimonio.delete()
        return redirect("matrimonios")

    return render(request, "matrimonios/eliminar.html", {"form": form, "id": id})
