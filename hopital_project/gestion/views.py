from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm

def liste_patients(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(prenom__icontains=query) | Patient.objects.filter(nom__icontains=query)
    else:
        patients = Patient.objects.all()

    return render(request, 'gestion/liste_patients.html', {'patients': patients, 'query': query})

# Ajouter un patient
def ajouter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = PatientForm()
    return render(request, 'gestion/ajouter_patient.html', {'form': form})

# Modifier un patient
def modifier_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'gestion/modifier_patient.html', {'form': form, 'patient': patient})

# Supprimer un patient
def supprimer_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('liste_patients')
    return render(request, 'gestion/supprimer_patient.html', {'patient': patient})
