from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect

from cuisine.ingredient.form_ingredient import IngredientForm, FrigoForm
from cuisine.models import Ingredient, Frigo


@login_required
@permission_required('cuisine.utiliser_ingredient')
def gestioningredient(request):
    ingredients = Ingredient.objects.all().order_by("nom")
    form_ajout = IngredientForm(request.POST or None)
    if form_ajout.is_valid():
        form_ajout.save()
        messages.success(request, "Ingrédient ajouté")
    return render(request, 'cuisine/gestionIngredients.html', locals())


@login_required
@permission_required('cuisine.gerer_frigo')
def gerer_ingredient_frigo(request):

    liste_element = Frigo.objects.all().order_by("ingredient")
    form_frigo = FrigoForm()

    if request.method == "POST":
        form_frigo = FrigoForm(request.POST, )
        if form_frigo.is_valid():
            if Frigo.objects.filter(ingredient=form_frigo.cleaned_data["ingredient"]).count() == 0:
                form_frigo.save()
                messages.success(request, "Ingrédient ajouté dans le frigo")
            else:
                liste_ingredient = Frigo.objects.filter(ingredient=form_frigo.cleaned_data["ingredient"]).all()
                for ingredient in liste_ingredient:
                    ingredient.quantite = form_frigo.cleaned_data["quantite"]
                    ingredient.unite = form_frigo.cleaned_data["unite"]
                    ingredient.save()
                messages.warning(request, "Cet ingrédient est déjà dans le frigo, il a été modifié")
    return render(request, 'cuisine/gererFrigo.html', locals())


@login_required
@permission_required('cuisine.gerer_frigo')
def modifier_ingredient_frigo(request, id_frigo):

    frigo_ingredient = get_object_or_404(Frigo, id=id_frigo)

    liste_element = Frigo.objects.all().order_by("ingredient")
    form_frigo = FrigoForm(request.POST or None, instance=frigo_ingredient)
    return render(request, 'cuisine/gererFrigo.html', locals())


@login_required
@permission_required('cuisine.gerer_frigo')
def effacer_ingredient_frigo(request, id_ingredient):
    ingredient = get_object_or_404(Frigo, id=id_ingredient)
    ingredient.delete()
    messages.warning(request, "Ingrédient enlevé du frigo")
    return redirect(gerer_ingredient_frigo)




