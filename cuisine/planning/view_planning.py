import locale
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from cuisine.course.view_course import ajouter_ingredient_bdd
from cuisine.models import Planning, Recette, RecetteIngredient
from cuisine.planning.form_planning import RecettePlanningForm


def accueil(request):
    locale.setlocale(locale.LC_ALL, locale="")
    date_jour = datetime.today()
    data = {}
    for i in range(0, 8):
        date = date_jour + timedelta(days=i)
        midi = []
        soir = []
        repas_midi = Planning.objects.filter(date=date, moment=1).all()
        repas_soir = Planning.objects.filter(date=date, moment=2).all()

        for j in range(1, 4):
            el_midi = [e for e in repas_midi if e.categorie == j]
            el_soir = [e for e in repas_soir if e.categorie == j]

            if len(el_midi) > 0:
                if el_midi[0].recette is not None:
                    midi.append(
                        ("/cuisine/planning/consulter/repas/{}".format(el_midi[0].id), el_midi[0].recette.titre))
                else:
                    midi.append(("/cuisine/planning/consulter/repas/{}".format(el_midi[0].id), el_midi[0].champ_libre))
            else:
                midi.append(
                    ("/cuisine/planning/ajouter/repas/{}/midi/{}".format(date.strftime("%Y%m%d"), j), "Ajouter"))

            if len(el_soir) > 0:
                if el_soir[0].recette is not None:
                    soir.append(
                        ("/cuisine/planning/consulter/repas/{}".format(el_soir[0].id), el_soir[0].recette.titre))
                else:
                    soir.append(("/cuisine/planning/consulter/repas/{}".format(el_soir[0].id), el_soir[0].champ_libre))
            else:
                soir.append(
                    ("/cuisine/planning/ajouter/repas/{}/soir/{}".format(date.strftime("%Y%m%d"), j), "Ajouter"))

        data[date.strftime("%A %d %B")] = [midi, soir]
    print(data)
    return render(request, 'cuisine/accueil.html', {'data': data})


@login_required
@permission_required('cuisine.utiliser_liste_course')
def ajouter_recette_planning(request, date, moment, type):
    if request.method == "POST":
        form = RecettePlanningForm(request.POST)
        if form.is_valid():
            recette = form.cleaned_data["recette"]
            champ_libre = form.cleaned_data["champ_libre"]
            date_a = form.cleaned_data["date_a"]
            date_b = form.cleaned_data["date_b"]
            moment = form.cleaned_data["moment"]
            categorie = form.cleaned_data["categorie"]

            if recette is not None:
                recette = Recette.objects.get(id=recette.id)
                recette.dateDernierePrepa = date_a
                recette.save()

                if form.cleaned_data["ajout_course"]:
                    liste_ingredient = RecetteIngredient.objects.filter(recette=recette).all()
                    for ingredient in liste_ingredient:
                        ajouter_ingredient_bdd(ingredient.ingredient, ingredient.quantite, ingredient.unite)

            planning = Planning(recette=recette, champ_libre=champ_libre, date=date_a, moment=moment,
                                categorie=categorie)
            planning.save()

            if date_b is not None:
                planning_b = Planning(recette=recette, champ_libre=champ_libre, date=date_b, moment=moment,
                                      categorie=categorie)
                planning_b.save()
            return redirect(accueil)
    else:
        date_convert = datetime.strptime(date, '%Y%m%d')
        data = {
            "moment": "1" if moment == "midi" else "2",
            "categorie": type,
            "date_a": date_convert,
        }
        form = RecettePlanningForm(initial=data)
    return render(request, "cuisine/ajouterRecettePlanning.html", {"date": date, "moment": moment, "type": type,
                                                                   "form": form})


@login_required
@permission_required('cuisine.utiliser_liste_course')
def consulter_recette_planning(request, id_planning):
    return render(request)


"""@login_required
@permission_required('cuisine.utiliser_liste_course')
def ajouter_recette_action(request, id_recette):

    if request.method == "POST":
        form_planning = RecetteCoursePlanningForm(request.POST)
        if form_planning.is_valid():
            if id_recette != 0:
                recette = Recette.objects.get(id=id_recette)
                recette.dateDernierePrepa = form_planning.cleaned_data['date_a']
                recette.save()

                liste_ingredient = RecetteIngredient.objects.filter(recette=recette).all()
                for ingredient in liste_ingredient:
                    ajouter_ingredient_bdd(ingredient.ingredient, ingredient.quantite, ingredient.unite)

            planning = Planning(recette=recette if id_recette != 0 else None,
                                date=form_planning.cleaned_data["date_a"],
                                categorie=form_planning.cleaned_data["categorie"],
                                moment=form_planning.cleaned_data["moment"],
                                champ_libre= form_planning.cleaned_data["champ_libre"] if id_recette == 0 else None)
            planning.save()

            return redirect(gestion_course)
    else:
        data = {'id_recette': id_recette,
                'moment': 2,
                'categorie': 2,
                'date_a': datetime.today().strftime("%d/%m/%Y")}
        form_planning = RecetteCoursePlanningForm(initial=data)

    if id_recette != 0:
        titre_recette = "Ajout de {}".format(Recette.objects.get(id=id_recette).titre)
        form_planning.fields['champ_libre'].widget = forms.HiddenInput()
    else:
        titre_recette = "Nouveau plat"
    return render(request, "cuisine/recetteCoursePlanning.html", {"id_rec": id_recette,
                                                             "form_planning": form_planning,
                                                             "recette": titre_recette})"""
