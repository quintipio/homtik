from django.urls import path
from . import views
from cuisine.autre_produit import view_autres_produits
from cuisine.ingredient import view_ingredient

urlpatterns = [
    path('accueil/', views.accueil, name="cuisineAccueil"),
    path('gestionProduits/', view_autres_produits.gestionproduits, name="gestionProduits"),
    path('gestionProduits', view_autres_produits.effacerproduit, name="effacerProduits"),
    path('gestionProduits/ajouter/', view_autres_produits.ajouterproduit, name="ajouter_produit"),
    path('gestionIngredients/', view_ingredient.gestioningredient, name="gestionIngredient"),
    path('gestionIngredients/ajouter/', view_ingredient.ajouteringredient, name="ajouter_ingredient"),
]