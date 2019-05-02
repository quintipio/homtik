from django import forms
from cuisine.models import Ingredient,Frigo


class IngredientForm(forms.ModelForm):
    nom = forms.CharField(error_messages={'unique': 'Cet ingrédient existe déjà'})

    def clean_nom(self):
        return self.cleaned_data['nom'].lower().capitalize()

    class Meta:
        model = Ingredient
        exclude = ()


class FrigoForm(forms.ModelForm):

    class Meta:
        model = Frigo
        exclude = ()
