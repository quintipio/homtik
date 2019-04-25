from django import forms
from cuisine.models import Ingredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ()
