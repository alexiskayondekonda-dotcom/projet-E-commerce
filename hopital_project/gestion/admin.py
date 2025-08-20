from django.contrib import admin
from .models import Patient, Medecin, Service

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Service)
