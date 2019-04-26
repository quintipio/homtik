from django import forms

from cuisine.models import Recette, RecetteIngredient


class RecetteForm(forms.ModelForm):
    error_css_class = "alert alert-errors"

    class Meta:
        model = Recette
        exclude = ("ingredients",)
        widgets = {
            'contenu': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'titre': forms.TextInput(attrs={'size': 15}),
            'tempsPreparation': forms.NumberInput(attrs={'size': 2}),
        }