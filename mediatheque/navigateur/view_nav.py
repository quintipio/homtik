import json

from django.http import HttpResponse
from django.shortcuts import render
import os

FOLDER_ROOT = "/home/vnps3445/Public"


def scan_folder(url: str):
    list_files = {}
    list_folder = {}
    for element in os.listdir(FOLDER_ROOT+url):
        if os.path.isdir(FOLDER_ROOT+url+element):
            list_folder[url+element+"/"] = element
        else:
            list_files[url+element] = element
    return list_files, list_folder


def accueil(request):
    list_files, list_folder = scan_folder("/")
    return render(request, "mediatheque/accueil.html", locals())


def load_folder(request):
    folder = request.POST['folder']
    list_files, list_folder = scan_folder(folder)
    data = {"list_files": list_files, "list_folder": list_folder}
    return HttpResponse(json.dumps(data))
