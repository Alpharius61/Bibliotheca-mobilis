from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class chaosAspectVenerated(models.Model):    
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"


class creationType(models.Model):
    name = models.CharField(max_length=10)
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