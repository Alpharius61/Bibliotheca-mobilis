from email.policy import default
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class accountCreationForm(UserCreationForm):
    
    origin =  forms.ChoiceField( choices = [("",""),("Chaos","Chaos"),("Imperium","Imperium"),("Xenos","Xeno")], required=True)

    # origin =  forms.ModelChoiceField(
    #     
    #     # queryset=userOrigin.objects.all(),
    #     widget=forms.Select(attrs={
    #         'class': 'form__control ',
    #     }),
    #     required=True
    # )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Pseudo ',
            'email': 'Email ',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'formClass',
            })

        self.fields['password1'].label = 'Mot de passe'
        self.fields['password2'].label = 'Confirmation de mot de passe'



class authentification():
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': 'Email ',
            'password': "Mot de passe",
        }