from django import forms
from django.contrib.auth.models import User
from registration.models import UserOrigine
from django.contrib.auth.forms import UserCreationForm


class accountCreationForm(UserCreationForm):
    origine = forms.ModelChoiceField(
        queryset=UserOrigine.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form__control ',
        }),
        required=True
    )

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