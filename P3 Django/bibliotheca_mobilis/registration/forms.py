from django import forms
from django.contrib.auth.models import User
from registration.models import UserOrigine
from django.contrib.auth.forms import UserCreationForm


class signUpForm(UserCreationForm):
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
            'password1' : 'Mot de passe',
            'password2' : 'Confirmation de mot de passe',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'signUpFormClass',
            })
