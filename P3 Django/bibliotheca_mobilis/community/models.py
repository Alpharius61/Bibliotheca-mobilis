from django.db import models
from django.contrib.auth.models import User
from main.models import chaosAspectVenerated


# Create your models here


class characterModel(models.Model):

    class creationType(models.TextChoices):
        Personnel = 'Personnel'
        Historique = 'Historique'
    
    class creationSide(models.TextChoices):
        imperium = 'Imperium'
        chaos = 'Chaos'
        xeno = 'Xeno'

    class creationRace(models.TextChoices):
        spaceMarine  = 'Space Marine'
        custodes = 'Custodes'
        imperialGuard = 'Garde Imperial'
        mechanicum = 'Adeptus Mechanicus'
        imperialKnight = 'Chevalier Impérial'
        battleSister = 'Soeur de bataille'

        chaosSpaceMarine = 'Space Marine du chaos'
        demon ='Demon'
        renegadeGuard = 'Garde Renégat'
        renagadeKnight = 'Chevalier du chaos'

        Ork = 'Ork'
        Aeldari = 'Aeldari'
        Drukhari = 'Drukhari'
        Tau = 'Tau'
        
   
    name = models.CharField(max_length=50)
    biography = models.TextField(max_length=200)
    type = models.CharField(max_length=50, choices=creationType.choices)
    side = models.CharField(max_length=50, choices=creationSide.choices)
    race = models.CharField(max_length=50, choices=creationRace.choices)
    chaosAspect = models.ForeignKey(chaosAspectVenerated, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures = models.ImageField(null=True)

    

    def __str__(self):
        return f"{self.name}"