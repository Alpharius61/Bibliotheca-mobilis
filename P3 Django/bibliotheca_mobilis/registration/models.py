from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserOrigine(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name}"


class authentification(models.Model):
    Email = models.EmailField()
    