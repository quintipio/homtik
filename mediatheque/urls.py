from django.urls import path

from mediatheque.navigateur import view_nav

urlpatterns = [
    path('navigateur/', view_nav.accueil, name="mediathequeAccueil"),

]
