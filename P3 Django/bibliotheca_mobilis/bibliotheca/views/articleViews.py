from django.shortcuts import redirect, render
from bibliotheca.models import history
from django.template.loader import get_template

def bibliothecaArticle(request, name):

   return render(request, "bibliotheca/"+name+".html")
    