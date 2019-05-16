from django import forms
from django.forms import formset_factory

from cuisine.models import CourseAutre, CourseIngredient, Recette, Planning


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
    unite_course = forms.FloatField(required=True, widget=forms.HiddenInput())
    nb_frigo = forms.FloatField(required=True, widget=forms.HiddenInput())
    unite_frigo = forms.FloatField(required=True, widget=forms.HiddenInput())
    nb_final = forms.FloatField(required=True)
    unite_final = forms.CharField(required=True, widget=forms.HiddenInput())


ComparerFrigoFormset = formset_factory(ComparerFrigoForm, extra=0)


class RecettePlanningForm(forms.Form):
    id_recette = forms.IntegerField(required=False, widget=forms.HiddenInput())
    champ_libre = forms.CharField(label="Plat", required=False, max_length=300)
    date_a = forms.DateField(required=True, label="Date du repas")
    data_b = forms.DateField(required=False, label="Autre date du repas")
    categorie = forms.ChoiceField(choices=Planning.CATEGORIE_CHOICE, required=True, label="Type de plat")
    moment = forms.ChoiceField(choices=Planning.MOMENT_CHOICE, required=True, label="Type de repas")
