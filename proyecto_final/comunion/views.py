from django.shortcuts import render, redirect


from .models import Comunion


def comuniones(request):
    comuniones_all = Comunion.objects.all()
    return render(request, "comunion/index.html", {"comuniones": comuniones_all})


def buscar_comunion(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        comuniones = (
            Comunion.objects.filter(nombre__icontains=busqueda)
            | Comunion.objects.filter(padre__icontains=busqueda)
            | Comunion.objects.filter(madre__icontains=busqueda)
            | Comunion.objects.filter(parroquia_bautizo__icontains=busqueda)
        )
    else:
        comuniones = Comunion.objects.all()

    return render(
        request,
        "comunion/index.html",
        {"comuniones": comuniones, "busqueda": busqueda},
    )


def crear_comunion(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        sexo_str = request.POST.get("sexo")
        sexo = True if sexo_str == "true" else False
        padre = request.POST.get("padre")
        madre = request.POST.get("madre")
        padrino_madrina = request.POST.get("padrino_madrina")
        ciudad_bautizo = request.POST.get("ciudad_bautizo")
        parroquia_bautizo = request.POST.get("parroquia_bautizo")
        fecha_bautizo = request.POST.get("fecha_bautizo")

        comunion = Comunion(
            nombre=nombre,
            sexo=sexo,
            padre=padre,
            madre=madre,
            padrino_madrina=padrino_madrina,
            ciudad_bautizo=ciudad_bautizo,
            parroquia_bautizo=parroquia_bautizo,
            fecha_bautizo=fecha_bautizo,
        )
        comunion.save()

    return redirect("comuniones")


def eliminar_comunion(request, id):
    comunion = Comunion.objects.get(id=id)

    comunion.delete()

    return redirect("comuniones")


def editar_comunion(request, id):
    comuniones = Comunion.objects.all()

    comunion = Comunion.objects.get(id=id)

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        sexo_str = request.POST.get("sexo")
        sexo = True if sexo_str == "true" else False
        padre = request.POST.get("padre")
        madre = request.POST.get("madre")
        padrino_madrina = request.POST.get("padrino_madrina")
        ciudad_bautizo = request.POST.get("ciudad_bautizo")
        parroquia_bautizo = request.POST.get("parroquia_bautizo")
        fecha_bautizo = request.POST.get("fecha_bautizo")

        comunion.nombre = nombre
        comunion.sexo = sexo
        comunion.padre = padre
        comunion.madre = madre
        comunion.padrino_madrina = padrino_madrina
        comunion.ciudad_bautizo = ciudad_bautizo
        comunion.parroquia_bautizo = parroquia_bautizo
        comunion.fecha_bautizo = fecha_bautizo
        comunion.save()

        return redirect("registrar_comunion")

    return render(
        request,
        "comunion/editar.html",
        {"comunion": comunion, "comuniones": comuniones, "comunion_editar": True},
    )
