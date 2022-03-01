from django.db import models

# Create your models here.

class chaosAspectVenerated(models.TextChoices):
    undivided = 'Undivided'
    khorn = 'Khorn'
    nurgle = 'Nurgle'
    tzeentch = 'Tzeentch'
    slannesh = 'Slannesh'