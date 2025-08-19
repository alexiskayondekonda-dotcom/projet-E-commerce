from django.shortcuts import render
from .models import Client
from commande.filters import CommandeFilter
from django.contrib.auth.decorators import login_required






@login_required(login_url='acces')
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()

  
    myFilter = CommandeFilter(request.GET, queryset=commande)
    commande = myFilter.qs  

    context = {
        'client': client,
        'commande': commande,
        'commande_total': commande_total,
        'myFilter': myFilter
    }
    return render(request, 'client/list_client.html', context)
