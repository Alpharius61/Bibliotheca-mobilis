from django.db import models
from django.contrib.auth.models import User

# Create your models here

class chaosAspectVenerated(models.Model):    
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"

class speciality(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class side(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"

class races(models.Model):
    name = models.CharField(max_length=25, validators=[])
    side = models.ForeignKey(side, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

