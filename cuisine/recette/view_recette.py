from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from cuisine.models import Recette, RecetteIngredient
from cuisine.recette.form_recette import RecetteForm


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
    form_ajout = RecetteForm(request.POST or None)
    titre = "Ajouter une recette"
    value_button = "Ajouter"
    return render(request,"cuisine/gererRecette.html", locals())


@login_required
def modifier_recette(request):
    return render(request)


@login_required
def effacer_recette(request):
    id = request.GET.get('toDel', None)
    recette = get_object_or_404(Recette, id=id)
    recette.delete()
    messages.warning(request, "Recette effacée")
    return render(request)