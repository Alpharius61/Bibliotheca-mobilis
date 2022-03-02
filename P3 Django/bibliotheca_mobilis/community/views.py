from django.shortcuts import redirect, render
# from community.models import characterCreationModel
# from main.models import chaosAspectVenerated
from community.forms import characterCreationForm
# Create your views here.

def characterCreationView(request):
 
    if request.method == 'POST':
        form = characterCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    
    context = {
        'form': form
    }

    return render(request, 'community/characterCreation.html', context)


