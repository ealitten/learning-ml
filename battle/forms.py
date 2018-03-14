from django import forms

from .models import Pokemon


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields('name').queryset = Pokemon.objects.none()
