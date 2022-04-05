from django.db import models
from django.forms import CharField

# Create your models here.

class histoiry (models.Model):

    parents = models.ForeignKey('self', on_delete = models.CASCADE,null=True, blank=True)
    content = models.TextField(max_length=100)
    title = models.CharField(max_length= 70)

    def __str__(self):
        return self.title
