from random import choice
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here

class chaosAspectVenerated(models.Model):    
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"

class specialities(models.Model):
    name = MultiSelectField(choices = models.CharField(max_length=50))
    def __str__(self):
        return f"{self.name}"

class creationSide(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"

class creationRace(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.name}"

class charactersModel(models.Model):

    historicCreation = models.BooleanField(default = False)
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=10000)
    speciality = models.ManyToManyField(specialities)
    side = models.ForeignKey(creationSide,on_delete=models.CASCADE)
    race = models.ForeignKey(creationRace, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE,null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to=("community\characterspictures"))

    def __str__(self):
        return f"{self.name}"


class armyModel(models.Model):

    historicCreation = models.BooleanField(default = False)
    name = models.CharField(max_length=50)
    history = models.TextField(max_length=10000)
    speciality = models.ManyToManyField(specialities)
    side = models.ForeignKey(creationSide,on_delete=models.CASCADE)
    race = models.ForeignKey(creationRace, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE, null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to=("community\characterspictures"))
    actualChef = models.CharField(max_length=50)
    firstChef = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
