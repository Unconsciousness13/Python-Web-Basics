from django.shortcuts import render
from django101.models import Person



def index(req):
    context = {
        'name': 'Spas',
        'people': Person.objects.all(),
        
    }
    return render(req, 'index.html',context)

def test(req):
    return render(req, 'test.html')