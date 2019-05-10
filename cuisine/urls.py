from django.urls import path
from . import views
from cuisine.autre_produit import view_autres_produits
from cuisine.ingredient import view_ingredient
from cuisine.recette import view_recette
from cuisine.course import view_course

urlpatterns = [
    path('', views.accueil, name="cuisineAccueil"),

    path('produits/', view_autres_produits.gestionproduits, name="gestion_produits"),
    path('produits/effacer/<int:id_produit>', view_autres_produits.effacerproduit, name="effacer_produits"),

    path('ingredients/', view_ingredient.gestioningredient, name="gestion_ingredient"),

    path('recette/', view_recette.gerer_recette, name="gerer_recette"),
    path('recette/effacer/<int:id_recette>', view_recette.effacer_recette, name="effacer_recette"),
    path('recette/<int:id_recette>', view_recette.consulter_recette, name="consulter_recette"),
    path('recette/modifier/<int:id_recette>', view_recette.modifier_recette, name="modifier_recette"),
    path('recette/ajouter/', view_recette.ajouter_recette, name="ajouter_recette"),

    path('frigo/', view_ingredient.gerer_ingredient_frigo, name="gerer_frigo"),
    path('frigo/effacer/<int:id_ingredient>', view_ingredient.effacer_ingredient_frigo,
         name="effacer_ingredient_frigo"),
    path('frigo/modifier/<int:id_frigo>', view_ingredient.modifier_ingredient_frigo
         , name="modifier_ingredient_frigo"),

    path('course/', view_course.gestion_course, name="gerer_course"),
    path('course/nouveau', view_course.nouvelle_course, name="nouvelle_course"),
    path('course/modifier/commentaire', view_course.modifier_commentaire, name="modifier_commentaire_course"),
    path('course/ajouter/produit', view_course.ajouter_autre, name="ajouter_produit_course"),
    path('course/ajouter/ingredient', view_course.ajouter_ingredient, name="ajouter_ingredient_course"),
    path('course/effacer/produit/<int:id_produit>', view_course.effacer_autre, name="effacer_produit_course"),
    path('course/effacer/ingredient/<int:id_ingredient>', view_course.effacer_ingredient,
         name="effacer_ingredient_course"),
    path('course/acheter/ingredient/<int:id_ingredient>', view_course.acheter_ingredient,
         name="acheter_ingredient_course"),
    path('course/acheter/produit/<int:id_produit>', view_course.acheter_produit,
         name="acheter_produit_course"),
    path('course/ajouter/recette/choix', view_course.ajouter_recette_choix,
         name="ajouter_recette_choix"),
    path('course/ajouter/recette/choix/<int:id_recette>', view_course.ajouter_recette_action,
         name="ajouter_recette_action"),
]
