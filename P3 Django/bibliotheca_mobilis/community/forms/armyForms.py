from django import forms
from community.models import armyModel, charactersModel, armyModel, speciality , races

class armyForm(forms.ModelForm):
    specialities = forms.ModelMultipleChoiceField(label = 'Spécialité(s)',
        widget=forms.CheckboxSelectMultiple, queryset=speciality.objects.all())

    class Meta:
        model = armyModel
        fields = ["historicCreation", "side", "race", "name", "chaosAspect",
                  "specialities", "actualChef", "firstChef", "history", "pictures"]
        labels = {
            'historicCreation': 'Création historique',
            'side': 'Camp ',
            'name': 'Nom ',
            'chaosAspect': 'Aspect du chaos vénéré ',
            'history': 'Histoire',
            'actualChef': 'Chef actuel',
            'firstChef': 'Premier chef',
            'pictures': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['side'].widget.attrs.update(
            {'onchange' : 'updateRaces(this.value);'}
        )
        
        self.fields['specialities'].widget.attrs.update(
            {'class': 'formClass specialityForm',
            'onclick' : 'checkCount(this.id);'}
        )

        self.fields['history'].widget.attrs.update(
            {'cols': '68'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })