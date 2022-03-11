from django.shortcuts import redirect, render
from community.forms import characterForm, armyForm
from community.models import charactersModel, armyModel, chaosAspectVenerated, speciality
from django.templatetags.static import static

# Create your views here.


def characterCreationView(request):
    form = characterForm()
    if request.method == 'POST':
        form = characterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            character.author = request.user
            character.save()

            for fieldSpeciality in request.POST['speciality']:
                characterSpeciality = speciality.objects.get(
                    id=fieldSpeciality)
                print(characterSpeciality)
                character.speciality.add(characterSpeciality)

            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'community/characterCreation.html', context)


def characterView(request, name):
    character = charactersModel.objects.get(name=name)
    context = {
        'character': character,
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


def armyCreationView(request):
    form = armyForm()
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

    return render(request, 'community/armyCreation.html', context)


def armyView(request, name):
    army = charactersModel.objects.get(name=name)
    context = {
        'army': army,
    }
    return render(request, 'community/army.html', context)


def armiesList(request):
    imperiumList = []
    chaosList = []
    xenoList = []

    armies = armyModel.objects.all()
    for army in armies:
        if str(army.side) == "Imperium":
            imperiumList.append(army)

        elif str(army.side) == "Chaos":
            chaosList.append(army)

        else:
            xenoList.append(army)

    context = {
        'imperiumList': imperiumList,
        'chaosList': chaosList,
        'xenoList': xenoList
    }
    return render(request, 'community/armiesList.html', context)
