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
                midi.append(el_midi[0].recette.titre if el_midi[0].recette is not None else el_midi[0].champ_libre)
            else:
                midi.append("{}/midi/{}".format(date.strftime("%Y%m%d"), j))

            if len(el_soir) > 0:
                soir.append(el_soir[0].recette.titre if el_soir[0].recette is not None else el_soir[0].champ_libre)
            else:
                soir.append("{}/soir/{}".format(date.strftime("%Y%m%d"), j))

        data[date.strftime("%A %d %B")] = [midi, soir]
    print(data)
    return render(request, 'cuisine/accueil.html', {'data': data})

