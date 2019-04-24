from django import forms
from cuisine.models import AutreProduit


class AutreProduitForm(forms.ModelForm):
    class Meta:
        model = AutreProduit
        exclude = ()
