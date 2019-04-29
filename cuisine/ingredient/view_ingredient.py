from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cuisine.ingredient.form_ingredient import IngredientForm
from cuisine.models import Ingredient


@login_required
def gestioningredient(request):
    ingredients = Ingredient.objects.all().order_by("nom")
    form_ajout = IngredientForm(request.POST or None)
    if form_ajout.is_valid():
        form_ajout.save()
        messages.success(request, "Ingrédient ajouté")
    return render(request, 'cuisine/gestionIngredients.html', locals())




