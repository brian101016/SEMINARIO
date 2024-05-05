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
