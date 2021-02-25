from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='access')
def list_Sensibilisation(request):
    return render(request,'sensibilisation/sensibilisation.html')