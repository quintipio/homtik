from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cuisine.autre_produit.form_autre_produit import AutreProduitForm
from cuisine.models import AutreProduit


@login_required
def gestionproduits(request):
    produits = AutreProduit.objects.all().order_by("nom")
    value_button_edit = "Ajouter"
    form_ajout = AutreProduitForm(request.POST or None)
    return render(request, 'cuisine/gestionProduits.html', locals())


@login_required
def effacerproduit(request):
    id_produit = request.GET.get('toDel', None)
    article = get_object_or_404(AutreProduit, id=id_produit)
    article.delete()
    messages.warning(request, "Produit effacé")
    return redirect(gestionproduits)


@login_required
def ajouterproduit(request):
    form = AutreProduitForm(request.POST or None)

    if form.is_valid():
        produit = form.save(commit=False)
        produit.save()
        form.save_m2m()
        messages.success(request, "Produit ajouté")
        value_button_edit = "Ajouter"
    return redirect(gestionproduits)

