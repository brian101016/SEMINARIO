from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from comunion.models import Comunion


def index(request):
    bautizos_total = 0  # Persona.objects.count()
    comuniones_total = Comunion.objects.count()
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


def bautizos_WIP(request):
    return HttpResponse("bautizos WIP")


def confirmaciones_WIP(request):
    return HttpResponse("confirmaciones WIP")


def matrimonios_WIP(request):
    return HttpResponse("matrimonios WIP")
