from django.shortcuts import render

from django101.models import Person


def index(req):
    context = {
        'name': 'Pako',
        'peopple':Person.objects.all(),
    }
    
    return render(req, 'index.html', context)