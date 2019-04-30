from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from cuisine.models import Recette, RecetteIngredient
from cuisine.recette.form_recette import RecetteForm, IngredientRecetteForm


def gerer_recette(request):
    recettes = Recette.objects.all().order_by("titre")
    return render(request, 'cuisine/gestionRecette.html', {"recettes": recettes})


def consulter_recette(request, id_recette):
    recette = Recette.objects.get(id=id_recette)
    ingredients = RecetteIngredient.objects.filter(recette=recette)
    calorie = range(recette.calorie)
    difficulte = range(recette.difficulte)
    return render(request, 'cuisine/visuRecette.html', locals())


@login_required
def ajouter_recette(request):
    titre = "Ajouter une recette"
    value_button = "Ajouter"

    ingredient_formset = formset_factory(IngredientRecetteForm, extra=2, min_num=1, max_num=30)

    if request.method == 'POST':

        recette_form = RecetteForm(request.POST, prefix="recet")
        ingredient_form = ingredient_formset(request.POST, prefix="ingred")

        if recette_form.is_valid() and ingredient_form.is_valid():
            recette = recette_form.save()
            for formset in ingredient_form:
                instance_formset = formset.save(commit=False)
                instance_formset.recette = recette
                instance_formset.save()
            messages.success(request, "Votre recette a bien été ajoutée")
            return redirect(gerer_recette)
    else:
        recette_form = RecetteForm(prefix="recet")
        ingredient_form = ingredient_formset(prefix="ingred")
    return render(request, "cuisine/gererRecette.html", {"recette_form": recette_form,
                                                         "ingredient_form": ingredient_form,
                                                         "titre": titre, "value_button": value_button})


@login_required
def modifier_recette(request):
    return render(request)


@login_required
def effacer_recette(request, id_recette):
    recette = get_object_or_404(Recette, id=id_recette)
    recette.delete()
    messages.warning(request, "Recette effacée")
    return redirect(gerer_recette)
