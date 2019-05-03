from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from general.views import connexion


def AuthRequiredMiddleware(get_response):

    def middleware(request):
        if   request.user and not request.user.is_authenticated():
            return HttpResponseRedirect(redirect(connexion))
        return None

    return middleware