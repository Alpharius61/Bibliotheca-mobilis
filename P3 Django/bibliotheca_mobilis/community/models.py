from django.db import models
from django.contrib.auth.models import User
from main.models import chaosAspectVenerated, creationRace, creationSide, creationType


# Create your models here


class charactersModel(models.Model):

    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=10000)
    type = models.ForeignKey(creationType, on_delete=models.CASCADE)
    side = models.ForeignKey(creationSide,on_delete=models.CASCADE)
    race = models.ForeignKey(creationRace, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE,null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to=("community\characterspictures"))

    def __str__(self):
        return f"{self.name}"


class armyModel(models.Model):

    name = models.CharField(max_length=50)
    history = models.TextField(max_length=10000)
    type = models.ForeignKey(creationType, on_delete=models.CASCADE)
    side = models.ForeignKey(creationSide,on_delete=models.CASCADE)
    race = models.ForeignKey(creationRace, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE, null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to=("community\characterspictures"))
    actualChef = models.CharField(max_length=50)
    firstChef = models.CharField(max_length=50, null=True, blank=True)
    speciality = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f"{self.name}"
