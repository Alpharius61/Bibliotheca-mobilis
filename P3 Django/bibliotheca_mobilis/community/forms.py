from re import S
from django import forms
from community.models import armyModel
from community.models import charactersModel, armyModel, speciality


class characterForm(forms.ModelForm):
    speciality = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=speciality.objects.all())

    class Meta:
        model = charactersModel
        fields = ["historicCreation", "side", "race", "name",
                  "chaosAspect", "speciality", "biography", "pictures"]
        labels = {
            'type': 'Type ',
            'side': 'Camp ',
            'name': 'Nom ',
            'chaosAspect': 'Aspect du chaos vénéré ',
            'speciality': 'Spécialité(s)',
            'biography': 'Biographie',
            'pictures': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['speciality'].widget.attrs.update(
            {'class': 'formClass specialityForm'},

        )

        self.fields['biography'].widget.attrs.update(
            {'cols': '68'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })



class armyForm(forms.ModelForm):
    speciality = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=speciality.objects.all())

    class Meta:
        model = armyModel
        fields = ["historicCreation", "side", "race", "name", "chaosAspect",
                  "speciality", "actualChef", "firstChef", "history", "pictures"]
        labels = {
            'historicCreation': 'Création historique',
            'side': 'Camp ',
            'name': 'Nom ',
            'chaosAspect': 'Aspect du chaos vénéré ',
            'history': 'Histoire',
            'actualChef': 'Chef actuel',
            'firstChef': 'Premier chef',
            'speciality': 'Spécialité(s)',
            'pictures': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['speciality'].widget.attrs.update(
            {'class': 'formClass specialityForm',
            'onclick' : 'checkCount(this.id);'}
        )

        self.fields['history'].widget.attrs.update(
            {'cols': '68'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })
