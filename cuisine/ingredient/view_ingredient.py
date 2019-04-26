from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cuisine.ingredient.form_ingredient import IngredientForm
from cuisine.models import Ingredient


@login_required
def gestioningredient(request):
    ingredients = Ingredient.objects.all().order_by("nom")
    form_ajout = IngredientForm(request.POST or None)
    return render(request, 'cuisine/gestionIngredients.html', locals())



@login_required
def ajouteringredient(request):
    form = IngredientForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Ingrédient ajouté")
    return redirect(gestioningredient)

