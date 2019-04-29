from django import forms
from cuisine.models import AutreProduit


class AutreProduitForm(forms.ModelForm):

    def clean_nom(self):
        return self.cleaned_data['nom'].lower().capitalize()

    class Meta:
        model = AutreProduit
        exclude = ()
