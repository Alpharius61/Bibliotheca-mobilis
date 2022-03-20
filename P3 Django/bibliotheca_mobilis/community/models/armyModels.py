from django.db import models
from django.contrib.auth.models import User
from .models import *

class armyModel(models.Model):

    historicCreation = models.BooleanField(default = False)
    name = models.CharField(max_length=50)
    history = models.TextField(max_length=10000)
    speciality = models.ManyToManyField(speciality)
    side = models.ForeignKey(creationSide,on_delete=models.CASCADE)
    race = models.ForeignKey(creationRace, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE, null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to=("community/armypictures"))
    actualChef = models.CharField(max_length=50)
    firstChef = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
