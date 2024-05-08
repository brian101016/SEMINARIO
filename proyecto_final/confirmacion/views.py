from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Confirmacion
from .forms import CrearConfirmacion, ConfirmacionForm


def index(request):
    confirmaciones = Confirmacion.objects.all()
    return render(
        request, "confirmacion/index.html", {"confirmaciones": confirmaciones}
    )


def crear_confirmacion(request):
    if request.method == "GET":
        return render(request, "confirmacion/crear.html", {"form": CrearConfirmacion()})
    else:
        Confirmacion.objects.create(
            nombre=request.POST["nombre"],
            sexo=request.POST["sexo"],
            padre=request.POST["padre"],
            madre=request.POST["madre"],
            padrino_madrina=request.POST["padrino_madrina"],
            parroquia_bautizo=request.POST["parroquia_bautizo"],
            ciudad_bautizo=request.POST["ciudad_bautizo"],
        )
        return redirect("confirmaciones")


def editar_confirmacion(request, id):
    if request.method == "GET":
        db_data = get_object_or_404(Confirmacion, pk=id)
        form = ConfirmacionForm(instance=db_data)
        return render(
            request,
            "confirmacion/editar.html",
            {"form": form, "confirmaciones": db_data},
        )
    else:
        db_data = get_object_or_404(Confirmacion, pk=id)
        sexo = request.POST["sexo"]
        db_data.sexo = sexo
        db_data.save()
        form = ConfirmacionForm(request.POST, instance=id)
        form.save()
        return redirect("confirmaciones")


def eliminar_confirmacion(request, id):
    db_data = Confirmacion.objects.filter(id=id)
    db_data.delete()
    return redirect("confirmaciones")
