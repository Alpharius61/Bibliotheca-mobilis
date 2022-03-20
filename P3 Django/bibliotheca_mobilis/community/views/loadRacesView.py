from django.shortcuts import render
from community.models import races

def load_races(request):
    side_id = request.GET.get('sideId')
    racesList = races.objects.filter(side_id=side_id).order_by('name')
    # races = creationRace.objects.order_by('name')
    return render(request, 'community/race_dropdown_list_options.html', {'races': racesList})