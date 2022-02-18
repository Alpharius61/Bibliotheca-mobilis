from django.shortcuts import render
from registration.forms import signUpForm

# Create your views here.


def signup(request):
    form = signUpForm
    if request.method == 'POST':
        print(request.POST)

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)
