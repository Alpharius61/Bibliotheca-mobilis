from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class signUp(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     origine = models.CharField(max_length=10, choices=origine.choices)

#     def __str__(self) -> str:
#         return f'{self.origine}'


class UserOrigine(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name}"
