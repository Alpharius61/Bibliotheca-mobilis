from django.db import models

# Create your models here.

class chaosAspectVenerated(models.TextChoices):

    Universel = 'undivided'
    Khorn = 'khorn'
    Nurgle = 'nurgle'
    Tzeentch = 'tzeentch'
    Slannesh = 'slannesh'


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