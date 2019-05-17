import calendar

from django.shortcuts import render
from datetime import datetime, timedelta
import locale

from cuisine.models import Planning


def accueil(request):
    locale.setlocale(locale.LC_ALL, locale="")
    date_jour = datetime.today()
    data = {}
    for i in range(0, 8):
        date = date_jour + timedelta(days=i)
        midi = []
        soir = []
        repas_midi = Planning.objects.filter(date=date, moment=1).all()
        repas_soir = Planning.objects.filter(date=date, moment=2).all()

        for j in range(1, 4):
            el_midi = [e for e in repas_midi if e.categorie == j]
            el_soir = [e for e in repas_soir if e.categorie == j]

            if len(el_midi) > 0:
                if el_midi[0].recette is not None:
                    midi.append(("planning/modifier/{}".format(el_midi[0].id), el_midi[0].recette.titre))
                else:
                    midi.append(("planning/modifier/{}".format(el_midi[0].id), el_midi[0].champ_libre))
            else:
                midi.append(("{}/midi/{}".format(date.strftime("%Y%m%d"), j), "Ajouter"))

            if len(el_soir) > 0:
                if el_soir[0].recette is not None:
                    soir.append(("planning/modifier/{}".format(el_soir[0].id), el_soir[0].recette.titre))
                else:
                    soir.append(("planning/modifier/{}".format(el_soir[0].id), el_soir[0].champ_libre))
            else:
                soir.append(("{}/soir/{}".format(date.strftime("%Y%m%d"), j), "Ajouter"))

        data[date.strftime("%A %d %B")] = [midi, soir]
    print(data)
    return render(request, 'cuisine/accueil.html', {'data': data})

