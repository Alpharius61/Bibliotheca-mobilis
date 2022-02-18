from django import forms
from registration.models import signUp

class signUpForm(forms.ModelForm):
    class Meta:
        model = signUp
        fields = ['pseudo','email','origine']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'signUpFormClass',
            })