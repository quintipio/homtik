from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from cuisine.course.form_course import CommentaireForm, AutreForm, IngredientForm
from cuisine.models import ListeCourse, CourseIngredient, CourseAutre, Unite


def gestion_course(request):
    liste = ListeCourse.objects.first()

    data = {'commentaire': liste.commentaire}
    commentaire_form = CommentaireForm(initial=data)
    produit_form = AutreForm()
    ingredient_form = IngredientForm()

    liste_autre = CourseAutre.objects.filter(listeCourse=liste).all()
    liste_ingredient = CourseIngredient.objects.filter(listeCourse=liste).all()

    return render(request, 'cuisine/listeCourse.html', locals())


@login_required
@permission_required('cuisine.effacer_liste_course')
def nouvelle_course(request):
    ListeCourse.objects.all().delete()
    CourseIngredient.objects.all().delete()
    CourseAutre.objects.all().delete()

    liste = ListeCourse(nom="Liste du {}/{}/{}".format(datetime.now().day, datetime.now().month, datetime.now().year),
                        commentaire="")
    liste.save()
    return redirect(gestion_course)

@login_required
@permission_required('cuisine.utiliser_liste_course')
def modifier_commentaire(request):
    form = CommentaireForm(request.POST)

    if form.is_valid():
        liste = ListeCourse.objects.first()
        liste.commentaire = form.cleaned_data['commentaire']
        liste.save()
        messages.success(request, "Commentaire ajouté")
    return redirect(gestion_course)


@login_required
@permission_required('cuisine.utiliser_liste_course')
def ajouter_autre(request):
    form = AutreForm(request.POST)

    if form.is_valid():
        if CourseAutre.objects.filter(autre=form.cleaned_data['autre']).count() > 0:
            autre_deja_present = CourseAutre.objects.get(autre=form.cleaned_data['autre'])
            autre_deja_present.nombre = autre_deja_present.nombre + " " + form.cleaned_data["nombre"]
            autre_deja_present.save()
        else:
            produit = form.save(commit=False)
            produit.listeCourse = ListeCourse.objects.first()
            produit.save()
        messages.success(request, "Produit ajouté")
    return redirect(gestion_course)


@login_required
@permission_required('cuisine.utiliser_liste_course')
def ajouter_ingredient(request):
    form = IngredientForm(request.POST)

    if form.is_valid():

        if CourseIngredient.objects.filter(ingredient=form.cleaned_data["ingredient"]).count() > 0:
            ing_dej_present = CourseIngredient.objects.get(ingredient=form.cleaned_data["ingredient"])
            ing_dej_present = additioner_course_ingredient(ing_dej_present,
                                                           form.cleaned_data["quantite"],
                                                           form.cleaned_data["unite"])
            ing_dej_present.save()
        else:
            ingredient = form.save(commit=False)
            ingredient.listeCourse = ListeCourse.objects.first()
            ingredient.save()
        messages.success(request, "Ingrédient ajouté")
    return redirect(gestion_course)


@login_required
@permission_required('cuisine.utiliser_liste_course')
def effacer_autre(request, id_produit):
    produit = get_object_or_404(CourseAutre, id=id_produit)
    produit.delete()
    messages.warning(request, "Produit effacé")
    return redirect(gestion_course)


@login_required
@permission_required('cuisine.utiliser_liste_course')
def effacer_ingredient(request, id_ingredient):
    ingredient = get_object_or_404(CourseIngredient, id=id_ingredient)
    ingredient.delete()
    messages.warning(request, "Ingrédient effacé")
    return redirect(gestion_course)


def acheter_ingredient(request, id_ingredient):
    ingredient = get_object_or_404(CourseIngredient, id=id_ingredient)
    ingredient.achete = not ingredient.achete
    ingredient.save()
    return redirect(gestion_course)


def acheter_produit(request, id_produit):
    produit = get_object_or_404(CourseAutre, id=id_produit)
    produit.achete = not produit.achete
    produit.save()
    return redirect(gestion_course)


def additioner_course_ingredient(ing_a: CourseIngredient, quant_b: float, unit_b: Unite):
    quant_a = ing_a.quantite
    unit_a = ing_a.unite

    # si les deux quantités font partie du même type d'unité
    if unit_a.unite_mere == unit_b.unite_mere \
            or unit_a.unite_mere == unit_b \
            or unit_b.unite_mere == unit_a \
            or unit_b == unit_a:

        # on mémorise l'unité en commun
        unit_princ = None
        if unit_a.unite_mere is not None:
            unit_princ = unit_a.unite_mere
        elif unit_b.unite_mere is not None:
            unit_princ = unit_b.unite_mere
        else:
            unit_princ = unit_a

        # on calcul la quantité en commun
        quant_unif = (quant_a * unit_a.quantite)+(quant_b * unit_b.quantite)

        # si le résultat est supérieur à 1, c'est que on doit prendre la quanité mère
        if quant_unif >= 1:
            ing_a.quantite = quant_unif
            ing_a.unite = unit_princ
        else:  # sinon il faut trouver laquelle prendre
            liste_unite_enfant = Unite.objects.filter(unite_mere=unit_princ).all().order_by('-quantite')
            # on prend chaque unité en partant de la plus grande, et si on obtient une quanite supérieur à zéro
            # on garde cette unité, sinon on garde la dernière unité
            for counter, value in enumerate(liste_unite_enfant):
                if quant_unif / value.quantite > 1 or counter == len(liste_unite_enfant):
                    ing_a.quantite = quant_unif
                    ing_a.unite = value
                    break
    return ing_a



