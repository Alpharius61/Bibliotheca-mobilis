from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from registration.forms import accountCreationForm , authentification

# Create your views here.


def accountCreation(request):
    form = accountCreationForm
    if request.method == 'POST':
        form = accountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    
    context = {
        'form': form
    }

    return render(request, 'registration/accountCreation.html', context)


def signUp(request):
    form = authentification()

    if request.method == 'POST':
        form = authentification(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/connection.html', context)