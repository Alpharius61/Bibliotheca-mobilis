from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from main.models import chaosAspectVenerated, creationRace, creationSide, creationType


# Create your models here


class charactersModel(models.Model):


    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=200)
    type = models.ForeignKey(creationType, on_delete=models.CASCADE)
    side = models.ForeignKey(creationSide, on_delete=models.CASCADE)
    race = models.ForeignKey(creationRace, on_delete=models.CASCADE)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures = models.ImageField(null=True, blank=True, upload_to=("community\characterspictures"))

    def __str__(self):
        return f"{self.name}"
