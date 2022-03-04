from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class chaosAspectVenerated(models.TextChoices):

    undivided = 'undivided',_("Universel")
    khorn = 'khorn',_("Khorn")
    nurgle = 'nurgle',_("Nurgle")
    tzeentch = 'tzeentch',_("Tzeentch")
    slannesh = 'slannesh',_("Slannesh")


class creationType(models.TextChoices):
    personnal = 'personnal',_("Personnel")
    historical = 'historical'

class creationSide(models.TextChoices):
    imperium = 'imperium',_("Imperium")
    chaos = 'chaos',_("Chaos")
    xeno = 'xeno',_("Xeno")

class creationRace(models.TextChoices):
    spaceMarine  = 'spaceMarine',_("Space Marine")
    custodes = 'custodes',_("Adeptus Custodes")
    astraMilitarum = 'astraMilitarum',_("Astra Militarum")
    adeptusMechanicus = 'adeptusMechanicus',_("Adeptus Mechanicus")
    imperialKnight = 'imperialKnight',_("Chevalier Impérial")
    battleSister = 'battleSister',_("Soeur de bataille")

    chaosSpaceMarine = 'chaosSpaceMarine',_("Space Marine du chaos")
    demon ='demon',_("Démon du chaos")
    chaosCultiste = 'chaosCultiste',_("Cultiste du Chaos")
    renagadeKnight = 'renagadeKnight',_("Chevalier du Chaos")

    ork = 'ork',_("Ork")
    aeldari = 'aeldari',_("Aeldari")
    drukhari = 'drukhari',_("Drukhari")
    tau = 'tau',_("Tau")