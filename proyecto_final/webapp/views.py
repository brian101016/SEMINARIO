from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


def index(request):
    # usuario = request.session.get("user", None)
    # if usuario == None:
    #     return redirect("login")

    bautizos_total = 0  # Persona.objects.count()
    comuniones_total = 0  # Persona.objects.count()
    confirmaciones_total = 0  # Persona.objects.count()
    matrimonios_total = 0  # Persona.objects.count()

    return render(
        request,
        "index.html",
        {
            "bautizos_total": f"\n({bautizos_total})",
            "comuniones_total": f"\n({comuniones_total})",
            "confirmaciones_total": f"\n({confirmaciones_total})",
            "matrimonios_total": f"\n({matrimonios_total})",
            "user": request.user,
        },
    )


from django.shortcuts import render, redirect
from comunion.models import Comunion


def principal(request):
    return render(request, "principal.html")


def datos_de_comunion(request):
    comuniones = Comunion.objects.all()
    return render(request, "datos_de_comunion.html", {"comuniones": comuniones})


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
        "datos_de_comunion.html",
        {"comuniones": comuniones, "busqueda": busqueda},
    )


def registrar_comunion(request):
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

    return redirect("datos_de_comunion")


def borrar_comunion(request, id):
    comunion = Comunion.objects.get(id=id)

    comunion.delete()

    return redirect("datos_de_comunion")


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
        "datos_de_comunion.html",
        {"comunion": comunion, "comuniones": comuniones, "comunion_editar": True},
    )
