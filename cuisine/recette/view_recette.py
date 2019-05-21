from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from cuisine.models import Recette, RecetteIngredient
from cuisine.recette.form_recette import RecetteForm, IngredientFormsetModif, IngredientFormsetAjout


def gerer_recette(request):
    recettes = Recette.objects.all().order_by("titre")
    return render(request, 'cuisine/gestionRecette.html', {"recettes": recettes})


def consulter_recette(request, id_recette):
    recette = Recette.objects.get_object_or_404(id=id_recette)
    ingredients = RecetteIngredient.objects.filter(recette=recette)
    calorie = range(recette.calorie)
    difficulte = range(recette.difficulte)
    return render(request, 'cuisine/visuRecette.html', locals())


@login_required
@permission_required('cuisine.utiliser_recette')
def ajouter_recette(request):
    titre = "Ajouter une recette"
    value_button = "Ajouter"
    
    ingredient_form = IngredientFormsetAjout(prefix="ingred")
    recette_form = RecetteForm(prefix="recet")

    if request.method == 'POST':

        recette_form = RecetteForm(request.POST, prefix="recet")
        ingredient_form = IngredientFormsetAjout(request.POST, prefix="ingred")

        if recette_form.is_valid() and ingredient_form.is_valid():
            recette = recette_form.save()
            for formset in ingredient_form:
                if "ingredient" in formset.cleaned_data and "quantite" in formset.cleaned_data:
                    instance_formset = formset.save(commit=False)
                    instance_formset.recette = recette
                    instance_formset.save()
            messages.success(request, "Votre recette a bien été ajoutée")
            return redirect(gerer_recette)
    return render(request, "cuisine/ajouterRecette.html", {"recette_form": recette_form,
                                                           "ingredient_form": ingredient_form,
                                                           "titre": titre,
                                                           "value_button": value_button})


@login_required
@permission_required('cuisine.modifier_recette')
def modifier_recette(request, id_recette):
    titre = "Modifier une recette"
    value_button = "Modifier"

    recette = get_object_or_404(Recette, id=id_recette)
    recette_form = RecetteForm(request.POST or None, prefix="recet", instance=recette)
    ingredient_form = IngredientFormsetModif(request.POST or None, prefix="ingred",
                                             queryset=RecetteIngredient.objects.filter(recette=recette))

    if request.method == "POST":
        if recette_form.is_valid() and ingredient_form.is_valid():
            recette_form.save()

            for formset in ingredient_form.deleted_forms:
                to_delete = formset.cleaned_data["id"]
                to_delete.delete()

            for formset in ingredient_form:
                if "ingredient" in formset.cleaned_data and "quantite" in formset.cleaned_data:
                    instance_formset = formset.save(commit=False)
                    instance_formset.recette = recette
                    instance_formset.save()

            messages.success(request, "Votre recette a bien été modifée")
            return redirect(gerer_recette)
    return render(request, "cuisine/modifierRecette.html", {"recette_form": recette_form,
                                                            "ingredient_form": ingredient_form,
                                                            "titre": titre,
                                                            "value_button": value_button,
                                                            "id_recette": id_recette})


@login_required
@permission_required('cuisine.modifier_recette')
def effacer_recette(request, id_recette):
    recette = get_object_or_404(Recette, id=id_recette)
    recette.delete()
    messages.warning(request, "Recette effacée")
    return redirect(gerer_recette)
