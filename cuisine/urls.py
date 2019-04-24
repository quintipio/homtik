from django.urls import path
from . import views
from cuisine.autre_produit import view_autres_produits

urlpatterns = [
    path('accueil/', views.accueil, name="cuisineAccueil"),
    path('gestionProduits/', view_autres_produits.gestionproduits, name="gestionProduits"),
    path('gestionProduits', view_autres_produits.effacerproduit, name="effacerProduits"),
    path('gestionProduits/ajouter/', view_autres_produits.ajouterproduit, name="ajouter_produit"),
]