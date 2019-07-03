import json

from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
import os

FOLDER_ROOT = "/home/vnps3445/Public"


def scan_folder(url: str):
    list_files = {}
    list_folder = {}

    if url != "/":
        list_folder[str(Path(url).parent)] = 'Dossier parent'

    for element in os.listdir(FOLDER_ROOT+url):
        if os.path.isdir(FOLDER_ROOT+url+element):
            list_folder[url+element+"/"] = element
        else:
            list_files[url+element] = element
    return list_files, list_folder


def accueil(request):
    return render(request, "mediatheque/accueil.html")


def load_folder(request):
    folder = request.POST['folder']
    if os.path.isfile(FOLDER_ROOT+folder):
        print("fichier")
    else :
        list_files, list_folder = scan_folder(folder)
        data = {"list_files": list_files, "list_folder": list_folder}
    return HttpResponse(json.dumps(data))
