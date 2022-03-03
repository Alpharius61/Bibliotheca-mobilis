from django.shortcuts import redirect, render
from main.models import chaosAspectVenerated
from community.forms import characterForm
from community.models import charactersModel
# Create your views here.


def characterCreationView(request):
    form = characterForm()
    if request.method == 'POST':
        form = characterForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'community/characterCreation.html', context)


def characterView(request, name):
    character = charactersModel.objects.get(name=name)
    context = {
        'character': character
    }
    return render(request, 'community/character.html', context)


def charactersList(request):
    characters = charactersModel.objects.all()
    print(characters)
    context = {
        'characters': characters
    }
    return render(request, 'community/communitiesCharacterList.html', context)
