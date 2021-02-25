from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Escroquerie
# Create your views here.
@login_required(login_url='access')
def list_Escroquerie(request):
    listEscroquerie = Escroquerie.objects.all()
    context = {"listEscroqueries": listEscroquerie}
    return render(request,'escroquerie/escroquerie.html',context)
