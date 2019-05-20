from django import forms

from cuisine.models import Planning, Recette


class RecettePlanningForm(forms.Form):
    recette = forms.ModelChoiceField(queryset=Recette.objects.all(), empty_label="Choisir une recette", required=False)
    ajout_course = forms.BooleanField(required=False, label="Ajouter les ingrédients à la liste de course : ")
    champ_libre = forms.CharField(label="sinon écrire le plat", required=False, max_length=300)
    date_a = forms.DateField(required=True, label="Date du repas")
    date_b = forms.DateField(required=False, label="Autre date du repas")
    categorie = forms.ChoiceField(choices=Planning.CATEGORIE_CHOICE, required=True, label="Type de plat")
    moment = forms.ChoiceField(choices=Planning.MOMENT_CHOICE, required=True, label="Type de repas")

    def clean(self):
        cleaned_data = super(RecettePlanningForm, self).clean()
        recette = cleaned_data.get("recette")
        champ_libre = cleaned_data.get("champ_libre")

        if champ_libre != "" and recette is not None:
            raise forms.ValidationError("On ne peut saisir et une recette et un champ libre")
