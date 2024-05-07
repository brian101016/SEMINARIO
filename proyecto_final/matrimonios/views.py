from django.shortcuts import render
from .models import Matrimonio
# Create your views here.


def matrimonios(request):
    matrimonios = Matrimonio.objects.all()
    return render(request, 'proyecto_final/',
    {'matrimonios': matrimonios})