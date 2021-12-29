from django.shortcuts import render

from django101.cities.models import Person


def index(req):
    context = {
        'name': 'Pako',
        'peopple':Person.objects.all(),
    }
    
    return render(req, 'index.html', context)

def test(req):
    return render(req, 'test.html')
    

# Create your views here.
