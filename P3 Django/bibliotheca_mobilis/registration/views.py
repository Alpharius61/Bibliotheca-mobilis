from multiprocessing import context
from django.shortcuts import render
from registration.models import signUp
from registration.forms import signUpForm

# Create your views here.
def signup(request):
    form = signUpForm
    if request.method == 'POST' :
        print(request.POST)

    context = {
        'form': form
    }
    
    return render (request, 'registration/signup.html', context)