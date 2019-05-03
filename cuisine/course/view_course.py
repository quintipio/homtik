from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from cuisine.course.form_course import CommentaireForm, AutreForm, IngredientForm
from cuisine.models import ListeCourse, CourseIngredient, CourseAutre


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






