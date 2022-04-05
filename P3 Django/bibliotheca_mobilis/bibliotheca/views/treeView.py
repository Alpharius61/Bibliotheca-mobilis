from django.shortcuts import redirect, render
from bibliotheca.models import history

def showTree(request):
    context = {
        "articles" : history.objects.all()
    }
    return render(request,"bibliotheca/tree.html", context)