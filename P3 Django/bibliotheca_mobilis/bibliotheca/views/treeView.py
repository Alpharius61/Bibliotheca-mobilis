from django.shortcuts import redirect, render
from bibliotheca.models import history
import logging

def showTree(request):
    logger = logging.getLogger('toto')
    rows = history.objects.all()
    logger.debug(rows)
    context = {
        'articles' : rows
    }

    return render(request,'bibliotheca/tree.html', context)