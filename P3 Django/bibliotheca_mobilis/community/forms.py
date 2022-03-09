from django import forms
from community.models import charactersModel


class characterForm(forms.ModelForm):
    
    class Meta:
        model = charactersModel
        fields = ["type","side","race","name","chaosAspect","biography","pictures"]
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
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })

class ArmyForm(forms.ModelForm):
    
    class Meta:
        model = charactersModel
        fields = ["type","side","race","name","chaosAspect","actualChef","firstChef","speciality","history","pictures"]
        labels = {
            'type': 'Type ',
            'side': 'Camp ',
            'name': 'Nom ',
            'chaosAspect': 'Aspect du chaos vénéré ',
            'history': 'Histoire',
            'actualChef' :'Chef actuel',
            'firstChef' : 'Premier chef',
            'speciality' : 'Spécialité',
            'pictures': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })
