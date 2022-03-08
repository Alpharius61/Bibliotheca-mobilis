from django.shortcuts import redirect, render
from main.models import chaosAspectVenerated
from community.forms import characterForm
from community.models import charactersModel
from django.templatetags.static import static

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
        'character': character,
    }
    return render(request, 'community/character.html', context)


def charactersList(request):
    imperiumList =[]
    chaosList = []
    xenoList=[]

    characters = charactersModel.objects.all()
    for character in characters:
        if str(character.side) =="Imperium" :
            imperiumList.append(character)
        
        elif str(character.side) =="Chaos" :
            chaosList.append(character)
        
        else :
            xenoList.append(character)
        
    context = {
        'imperiumList': imperiumList,
        'chaosList': chaosList,
        'xenoList': xenoList
    }
    return render(request, 'community/communitiesCharacterList.html', context)
