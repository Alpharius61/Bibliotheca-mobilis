from django import forms
from community.models import characterModel


class characterCreationForm(forms.ModelForm):
    
    class Meta:
        model = characterModel
        fields = ["type","side","race","name","chaosAspect","biography"]
