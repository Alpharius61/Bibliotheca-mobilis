from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class authentification(models.Model):
    Email = models.EmailField()
    