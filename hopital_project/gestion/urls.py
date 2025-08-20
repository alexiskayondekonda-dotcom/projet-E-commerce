from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_patients, name='liste_patients'),
    path('ajouter/', views.ajouter_patient, name='ajouter_patient'),
    path('modifier/<int:patient_id>/', views.modifier_patient, name='modifier_patient'),
    path('supprimer/<int:patient_id>/', views.supprimer_patient, name='supprimer_patient'),
]
