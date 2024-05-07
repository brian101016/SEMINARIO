from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Confirmacion
from .forms import CrearConfirmacion, ConfirmacionForm

def index(request):
    confirmaciones = Confirmacion.objects.all()
    return render(request, 'index.html', {'confirmaciones': confirmaciones})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {
        'forms' : CrearConfirmacion()
        })
    else:
        Confirmacion.objects.create(
            nombre=request.POST['nombre'],
            sexo = request.POST['sexo'],
            padre = request.POST['padre'],
            madre = request.POST['madre'],
            padrino_madrina = request.POST['padrino_madrina'],
            parroquia_bautizo = request.POST['parroquia_bautizo'],
            ciudad_bautizo = request.POST['ciudad_bautizo'],
        )
        return redirect('index')
    
def update(request,confirmacion_id):
    if request.method == 'GET':
        db_data = get_object_or_404(Confirmacion,pk = confirmacion_id)
        forms = ConfirmacionForm(instance=db_data)
        return render(request, 'update.html', {
            'forms' : forms,
            'confirmaciones': db_data})
    else:
        db_data = get_object_or_404(Confirmacion,pk = confirmacion_id)
        sexo = request.POST['sexo']
        db_data.sexo = sexo
        db_data.save()
        forms = ConfirmacionForm(request.POST,instance=db_data)
        forms.save()
        return redirect('index')

    
def delete(request,confirmacion_id):
    db_data = Confirmacion.objects.filter(id = confirmacion_id)
    db_data.delete()
    return redirect('index')

