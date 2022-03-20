from django.shortcuts import redirect, render
from community.forms import  armyForm
from community.models import armyModel, speciality
from django.templatetags.static import static

# Create your views here.

def armyCreationView(request):
    form = armyForm()
    if request.method == 'POST':
        form = armyForm(request.POST, request.FILES)
        if form.is_valid():
            army = form.save(commit=False)
            army.author = request.user
            army.save()
            for fieldSpeciality in request.POST['speciality']:
                armySpeciality = speciality.objects.get(
                    id=fieldSpeciality)
                print(armySpeciality)
                army.speciality.add(armySpeciality)
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'community/armyCreation.html', context)


def armyView(request, name):
    army = armyModel.objects.get(name=name)
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
