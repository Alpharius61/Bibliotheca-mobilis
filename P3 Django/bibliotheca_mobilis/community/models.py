from django.db import models
from django.contrib.auth.models import User
from main.models import chaosAspectVenerated, creationRace, creationSide, creationType


# Create your models here


class charactersModel(models.Model):

    class creationType(models.TextChoices):
        Personnel = 'Personnel'
        Historique = 'Historique'

    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=200)
    type = models.CharField(max_length=50, choices=creationType.choices)
    side = models.CharField(max_length=50, choices=creationSide.choices)
    race = models.CharField(max_length=50, choices=creationRace.choices)
    chaosAspect = models.CharField(
        null=True, blank=True, max_length=50, choices=chaosAspectVenerated.choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"
