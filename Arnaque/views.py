from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Arnaque
# Create your views here.
@login_required(login_url='access')
def list_Arnaque(request):
    listArnaque=Arnaque.objects.all()
    context={"listArnaques" : listArnaque}
    return render(request,'arnaque/arnaque.html',context)


