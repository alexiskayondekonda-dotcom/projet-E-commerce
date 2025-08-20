from django.db import models

class Patient(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def __str__(self):
        return f"{self.prenom} {self.nom}"


    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Service(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
prenom = models.CharField(max_length=100, default='Inconnu')
