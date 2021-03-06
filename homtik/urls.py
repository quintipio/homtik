"""homtik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from general import views as genview
from django.contrib.auth import views as auth_views

handler404 = genview.err404

urlpatterns = [
    path('', genview.accueil),
    path('admin/', admin.site.urls),
    path('accueil/', genview.accueil, name="accueil"),
    path('connexion/', genview.connexion, name="connexion"),
    path('accounts/login/', genview.connexion),
    path('deconnexion/', genview.deconnexion, name="deconnexion"),
    path('changermotdepasse/', auth_views.PasswordChangeView.as_view(), name="change_mdp"),
    path('resetMotDePasse/', auth_views.PasswordResetView.as_view(), name="reset_mdp"),

    path('cuisine/', include('cuisine.urls')),
    path('mediatheque/', include('mediatheque.urls')),
]
