from django import forms
from community.models import armyModel, charactersModel, armyModel, speciality , races

 


class characterForm(forms.ModelForm):
    specialities = forms.ModelMultipleChoiceField(label = 'Spécialité(s)',
        widget=forms.CheckboxSelectMultiple, queryset=speciality.objects.all())

    class Meta:
        model = charactersModel
        fields = ["historicCreation", "side", "race", "name",
                  "chaosAspect",'specialities',"biography", "pictures"]
        labels = {
            'type': 'Type ',
            'side': 'Camp ',
            'name': 'Nom ',
            'chaosAspect': 'Aspect du chaos vénéré ',
            'biography': 'Biographie',
            'pictures': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['race'].queryset = races.objects.none()

        self.fields['specialities'].widget.attrs.update(
            {'class': 'formClass specialityForm',
            'onclick' : 'checkCount(this.id);'}
        )
        self.fields['side'].widget.attrs.update(
            {'onchange' : 'updateRaces(this.value);'}
        )

        self.fields['biography'].widget.attrs.update(
            {'cols': '68'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })
        
        if 'side' in self.data:
            try:
                sideId = int(self.data.get('side'))
                self.fields['race'].queryset = races.objects.filter(side_id=sideId).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty race queryset
        elif self.instance.pk:
            self.fields['race'].queryset = self.instance.side.race_set.order_by('name')
