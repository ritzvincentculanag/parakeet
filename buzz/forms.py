from django import forms

from .models import Buzz


class BuzzCreateForm(forms.ModelForm):
    class Meta:
        model = Buzz
        fields = ['title', 'body', 'status']
