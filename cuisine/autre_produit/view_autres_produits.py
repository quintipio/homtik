from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from cuisine.autre_produit.form_autre_produit import AutreProduitForm
from cuisine.models import AutreProduit


@login_required
@permission_required('cuisine.utiliser_produit')
def gestionproduits(request):
    produits = AutreProduit.objects.all().order_by("nom")
    form_ajout = AutreProduitForm(request.POST or None)
    if form_ajout.is_valid():
        form_ajout.save()
        messages.success(request, "Produit ajouté")
    return render(request, 'cuisine/gestionProduits.html', locals())


@login_required
@permission_required('cuisine.modifier_produit')
def effacerproduit(request, id_produit):
    article = get_object_or_404(AutreProduit, id=id_produit)
    article.delete()
    messages.warning(request, "Produit effacé")
    return redirect(gestionproduits)

