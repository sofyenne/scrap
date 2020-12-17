from django.db import models

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    prix = models.FloatField()
    lien = models.CharField(max_length=300)
    marque = models.CharField(max_length=300)
    etat = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    site_officiel = models.CharField(max_length=200)
