from django.shortcuts import redirect, render
from community.forms.characterForms import characterForm
from community.models import charactersModel, speciality
import logging

def characterCreationView(request):
    logger = logging.getLogger('toto')
    form = characterForm()
    if request.method == 'POST':
        form = characterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            character.author = request.user
            character.save()
            for fieldSpeciality in request.POST.getlist('specialities'):
                characterSpeciality = speciality.objects.get(
                    id=fieldSpeciality)
                character.speciality.add(fieldSpeciality)
                
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'community/characterCreation.html', context)

def characterUpdate(request, id):
    logger = logging.getLogger('toto')
    character = charactersModel.objects.get(id=id)
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            character.delete()
            return redirect('/charactersList/')

        form = characterForm(request.POST, request.FILES, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.author = request.user
            character.save()
            for fieldSpeciality in request.POST.getlist('specialities'):
                characterSpeciality = speciality.objects.get(
                    id=fieldSpeciality)
                character.speciality.add(fieldSpeciality)    
    else :
        form =  characterForm(instance = character)

    context = {
        'form': form
    }
    return render (request,'community/characterUpdate.html', context )

def characterView(request, name):
    character = charactersModel.objects.get(name=name)
    authorId = character.author.id
    context = {
        'character': character,
        'authorId': authorId
    }
    return render(request, 'community/character.html', context)


def charactersList(request):
    imperiumList = []
    chaosList = []
    xenoList = []

    characters = charactersModel.objects.all()
    for character in characters:
        if str(character.side) == "Imperium":
            imperiumList.append(character)

        elif str(character.side) == "Chaos":
            chaosList.append(character)

        else:
            xenoList.append(character)

    context = {
        'imperiumList': imperiumList,
        'chaosList': chaosList,
        'xenoList': xenoList
    }
    return render(request, 'community/communitiesCharacterList.html', context)