from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import creerUtilisateur
from django.contrib import messages
 

def inscriptionPage(request):
    form = creerUtilisateur()
    if request.method=='POST':
        form = creerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter. " +user)
            return redirect('acces')
    context={'form':form}
    return render(request, 'compte/inscription.html',context)
 
def accesPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            message.info(request,"il ya une erreur dans le nonm d'utilisateur et/ou Mot de passe")
    return render(request, 'compte/acces.html',context)

def logoutUser(request):
    logout(request)
    return redirect('acces')


     