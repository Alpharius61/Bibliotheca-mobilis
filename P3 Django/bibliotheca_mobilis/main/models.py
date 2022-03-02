from django.db import models

# Create your models here.

class chaosAspectVenerated(models.Model):
    
    class chaosChoice(models.TextChoices):
        undivided = 'Undivided'
        khorn = 'Khorn'
        nurgle = 'Nurgle'
        tzeentch = 'Tzeentch'
        slannesh = 'Slannesh'

    chaosAspect = models.CharField(max_length=50, choices=chaosChoice.choices)