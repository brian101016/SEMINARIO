from django.shortcuts import render
from .models import Matrimonio
# Create your views here.

def mostrarMatrimonios(request):
    matrimonios = Matrimonio.objects.order_by('id')
    return render(request, 'templates\indexMatrimonio.html',
    {'matrimonios': matrimonios})

def nuevoMatrimonio(request):
    if request.method == 'POST':
        formaMatriomonio = MatriomonioForm(request.POST)

        if formaMatriomonio.is_valid():
            formaMatriomonio.save()
            return redirect('inicio')
        else:
            return render(request, 'templates\nuevoMatrimonio.html',
                          {'formaMatriomonio': formaMatriomonio})

def editarMatrimonio(request):
    matrimonio = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaMatriomonio = MatrimonioFrom(request.POST, instance=matrimonio)

        if formaMatriomonio.is_valid():
            formaMatriomonio.save()
            return redirect('inicio')
        else:
            return render(request,'templates/editarMatrimonio.html',
            {'formaMatrimonio': formaMatriomonio})


def eliminarMatrimonio(request, id):

    matrimonio = get_object_or_404(Matrimonio, pk=id)

    if matrimonio:
        matrimonio.delete()
        return redirect('inicio')
