from django.shortcuts import render, get_object_or_404, redirect
from .models import Matrimonio
from .forms import MatrimonioForm
# Create your views here.

from matrimonios.forms import MatrimonioForm

def mostrarMatrimonios(request):
    matrimonios = Matrimonio.objects.order_by('id')
    return render(request, 'indexMatrimonio.html',
    {'matrimonios': matrimonios})

def nuevoMatrimonio(request):
    if request.method == 'POST':
        formaMatrimonio = MatrimonioForm(request.POST)

        if formaMatrimonio.is_valid():
            formaMatrimonio.save()
            return redirect('index')
        else:
            return render(request, 'nuevoMatrimonio.html',
            {'formaMatrimonio': formaMatrimonio})
    else:
        formaMatrimonio = MatrimonioForm()
        return render(request, 'nuevoMatrimonio.html',
        {'formaMatrimonio': formaMatrimonio})

def editarMatrimonio(request, id):
    matrimonio = get_object_or_404(Matrimonio, id=id)
    if request.method == 'POST':
        formaMatrimonio = MatrimonioForm(request.POST, instance=matrimonio)

        if formaMatrimonio.is_valid():
            formaMatrimonio.save()
            return redirect('index')
        else:
            return render(request,'editarMatrimonio.html',
            {'formaMatrimonio': formaMatrimonio})
    else:
        matrimonio = get_object_or_404(Matrimonio, id=id)
        formaMatrimonio = MatrimonioForm(instance=matrimonio)
        return render(request,'editarMatrimonio.html',
        {'formaMatrimonio': formaMatrimonio})

def eliminarMatrimonio(request, id):

    matrimonio = Matrimonio.objects.filter(id = id)
    matrimonio.delete()
    return redirect('index')
