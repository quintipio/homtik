from django.urls import path

from mediatheque.navigateur import view_nav

urlpatterns = [
    path('navigateur/', view_nav.accueil, name="mediathequeAccueil"),
    path('navigateur/path/', view_nav.load_folder, name="mediathequeNavigue"),

]
