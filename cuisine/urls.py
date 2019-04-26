from django.urls import path
from . import views
from cuisine.autre_produit import view_autres_produits
from cuisine.ingredient import view_ingredient
from cuisine.recette import view_recette

urlpatterns = [
    path('accueil/', views.accueil, name="cuisineAccueil"),

    path('gestionProduits/', view_autres_produits.gestionproduits, name="gestionProduits"),
    path('gestionProduits', view_autres_produits.effacerproduit, name="effacerProduits"),
    path('gestionProduits/ajouter/', view_autres_produits.ajouterproduit, name="ajouter_produit"),

    path('gestionIngredients/', view_ingredient.gestioningredient, name="gestionIngredient"),
    path('gestionIngredients/ajouter/', view_ingredient.ajouteringredient, name="ajouter_ingredient"),

    path('gestionRecette/', view_recette.gerer_recette, name="gerer_recette"),
    path('gestionRecette', view_recette.effacer_recette, name="effacer_recette"),
    path('gestionRecette/<int:id_recette>', view_recette.consulter_recette, name="consulter_recette"),
    path('gestionRecette/modifier/<int:id_recette>', view_recette.modifier_recette, name="modifier_recette"),
    path('gestionRecette/ajouter/', view_recette.ajouter_recette, name="ajouter_recette"),
]