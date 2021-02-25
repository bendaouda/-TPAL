from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='access')
def list_Sextorsion(request):
    return render(request,'sextorsion/sextorsion.html')