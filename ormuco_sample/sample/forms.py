from django.forms import ModelForm
from sample.models import Person
from django import forms
from django.utils.translation import gettext as _

class SampleForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'favorite_color', 'cats_or_dogs']
        labels = {'name': _('Name'), 'favorite_color': _('Favorite Color'), 'cats_or_dogs': _('Cats or Dogs')}

    def clean_name(self):
        name = self.cleaned_data['name']
        if Person.objects.filter(name__iexact=name):
            raise forms.ValidationError("Name already exists")
        return name
    
    

    def save(self, commit=True):
        person = super().save(commit=False)
        if commit:
            person.save()
        return person