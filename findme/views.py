from django.shortcuts import render
from django.conf import settings
import pyrebase

config = {
    'apiKey': settings.API_KEY,
    'authDomain': settings.AUTH_DOMAIN,
    'databaseURL': settings.DATABASE_URL,
    'projectId': settings.PROJECT_ID,
    'storageBucket': settings.STORAGE_BUCKET,
    'messagingSenderId': settings.MESSAGING_SENDER_ID,
    'appId': settings.APP_ID
}
firebase = pyrebase.initialize_app(config)
authentication = firebase.auth()
database = firebase.database()


def index(request):
    return render(request, 'findme/index.html', {'map_api': settings.GOOGLE_MAP_API, })


def get_data(request):
    last_locations = list()
    for location in database.child('sensors').child('fZS0U-DtRumJebVn_6o6e-').child('locations').get().each():
        last_locations.append(location.val())
    context = {
        'name': database.child('sensors').child('fZS0U-DtRumJebVn_6o6e-').child('name').get().val(),
        'locations': last_locations,
        'marker': last_locations[-1],
    }

    return render(request, 'findme/ajax.html', context)
