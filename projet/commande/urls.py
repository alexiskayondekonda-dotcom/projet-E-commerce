from django.urls import path
from .import views

urlpatterns = [
    path('',views.list_commande, name='list_commande'),
    path('ajout_commande/',views.ajouter_commande,name='ajout_commande'),
    path('commandes/modifier/<int:pk>/', views.modifier_commande, name='modifier_commande'),
    path('commandes/supprimer/<int:pk>/', views.supprimer_commande, name='supprimer_commande'),

   
]
