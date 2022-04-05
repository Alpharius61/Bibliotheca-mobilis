from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class history(MPTTModel):
    
    name = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length= 70)
    parent = TreeForeignKey('self', on_delete = models.CASCADE,null=True, blank=True, related_name='children')
    contentURL = models.TextField(max_length=100)
    
    class MPTTMETA:
        oder_insertion_by = ['name']

    def __str__(self):
        return self.title
