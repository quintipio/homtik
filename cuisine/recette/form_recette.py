from django import forms
from django.forms import modelformset_factory

from cuisine.models import Recette, RecetteIngredient


class RecetteForm(forms.ModelForm):

    class Meta:
        model = Recette
        exclude = ("ingredients",)
        widgets = {
            'contenu': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'titre': forms.TextInput(attrs={'size': 15}),
            'tempsPreparation': forms.NumberInput(attrs={'size': 2}),
        }


IngredientFormset = modelformset_factory(RecetteIngredient, extra=2, min_num=1, max_num=30, exclude=("recette",))
