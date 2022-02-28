import imp


import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from registration.forms import accountCreationForm , auth
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


def connection(request):
    form = auth()
    logger = logging.getLogger('toto')
    if request.method == 'POST':
        logger.debug ("""connection: request.method = 'POST'""")
        form = auth(data=request.POST)

        if form.is_valid():
            logger.debug ("""connection: form is valid""")                        
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])            
            if user is not None :                
                logger.debug (user)
                login(request, user)
                return redirect('/')
        else:            
            logger.debug ("""connection: form NOT is valid""")
            logger.debug ("form error=%s, form.non_field_errors=%s" % (form.errors, form.non_field_errors))
    context = {'form': form}
    return render(request, 'registration/connection.html', context)

def logOut(request):
    logout(request)
    return redirect('/')