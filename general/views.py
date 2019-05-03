from django.shortcuts import render, redirect
from django.contrib.auth import logout,login, authenticate
from general.forms import ConnexionForm


def accueil(request):
    return render(request, 'general/accueil.html')


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(accueil)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'general/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(connexion)


def err404(request, exception):
    return render(request, "general/err404.html")
