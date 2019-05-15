from django import forms
from django.forms import formset_factory

from cuisine.models import CourseAutre, CourseIngredient, Recette


class CommentaireForm(forms.Form):
    commentaire = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))


class AutreForm(forms.ModelForm):

    class Meta:
        model = CourseAutre
        exclude = ('listeCourse', 'achete')


class IngredientForm(forms.ModelForm):

    class Meta:
        model = CourseIngredient
        exclude = ('listeCourse', 'achete')


class AjoutRecetteSimpleForm(forms.Form):
    recette_choisie = forms.ModelChoiceField(queryset=Recette.objects.all(), empty_label="Choisir une recette")


class AjoutRecetteRechercheForm(forms.Form):
    calorie = forms.ChoiceField(choices=Recette.CALORIE_CHOICE, required=False)
    categorie = forms.ChoiceField(choices=Recette.CATEGORIE_CHOICE, required=False)
    difficulte = forms.ChoiceField(choices=Recette.DIFFICULTE_CHOICE, required=False)


class ComparerFrigoForm(forms.Form):
    id = forms.FloatField(required=True, widget=forms.HiddenInput())
    ingredient = forms.CharField(required=True, widget=forms.HiddenInput())
    nb_course = forms.FloatField(required=True, widget=forms.HiddenInput())
    nb_frigo = forms.FloatField(required=True, widget=forms.HiddenInput())
    nb_final = forms.FloatField(required=True)
    unite_final = forms.CharField(required=True, widget=forms.HiddenInput())


ComparerFrigoFormset = formset_factory(ComparerFrigoForm, extra=0)
