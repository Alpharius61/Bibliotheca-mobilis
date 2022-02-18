import email
from random import choices
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class signUp(models.Model):

    class origine(models.TextChoices):
        Chaos = 'Chaos'
        Imperial ='Imperial'
        Xeno ='Xeno'

    pseudo = models.CharField (max_length=50)
    email = models.EmailField()
    password = PasswordInput()
    origine = models.TextField(choices=origine.choices)

    def __str__(self) -> str:
        return f'{self.name}'