from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User


from bautizos.models import Bautizo
from comuniones.models import Comunion
from confirmaciones.models import Confirmacion
from matrimonios.models import Matrimonio


def index(request):
    """Página principal del sistema.

    Muestra la cantidad de registros existentes de cada modelo y permite
    acceder rápidamente al resto de módulos y funcionalidades.
    """

    bautizos_total = Bautizo.objects.count()
    comuniones_total = Comunion.objects.count()
    confirmaciones_total = Confirmacion.objects.count()
    matrimonios_total = Matrimonio.objects.count()
    usuarios_total = User.objects.count()

    return render(
        request,
        "index.html",
        {
            "bautizos_total": f"\n({bautizos_total})",
            "comuniones_total": f"\n({comuniones_total})",
            "confirmaciones_total": f"\n({confirmaciones_total})",
            "matrimonios_total": f"\n({matrimonios_total})",
            "usuarios_total": f"\n({usuarios_total})",
        },
    )
