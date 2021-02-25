from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Acceuil
# Create your views here.
@login_required(login_url='acces')
def home(request):
    listAcceuil = Acceuil.objects.all()
    context = {"listAcceuils": listAcceuil}
    return render(request,'acceuil/acceuil.html',context )
