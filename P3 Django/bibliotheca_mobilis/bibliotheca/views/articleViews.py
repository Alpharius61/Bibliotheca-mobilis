from django.shortcuts import redirect, render
from bibliotheca.models import histoiry

def bibliothecaArticle(request,id):
   
   return render(request, 'bibliotheca/{{h ystory.name}}.html')
    