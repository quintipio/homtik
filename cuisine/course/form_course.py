from django import forms
from cuisine.models import Ingredient, Frigo, CourseAutre, CourseIngredient


class CommentaireForm(forms.Form):
    commentaire = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))


class AutreForm(forms.ModelForm):

    class Meta:
        model = CourseAutre
        exclude = ('listeCourse',)


class IngredientForm(forms.ModelForm):

    class Meta:
        model = CourseIngredient
        exclude = ('listeCourse',)