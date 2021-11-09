from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {
        'map_api': settings.GOOGLE_MAP_API,
    }
    return render(request, 'findme/index.html', context)
