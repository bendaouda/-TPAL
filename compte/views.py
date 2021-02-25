from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.forms  import UserCreationForm
from .forms import creerUtilisateur

# Create your views here.
from django.shortcuts import render

# Create your views here.
def inscriptionPage(request):
    form= creerUtilisateur()
    if request.method=='POST':
        form=creerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'compte crée avec succés')
            return redirect('acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

def accesPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password,)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.info(request, "Utilisateur et mot de passe incorrects")

    return render(request,'compte/acces.html',context)

def logoutUser(request):
    logout(request)
    return redirect('acces')
