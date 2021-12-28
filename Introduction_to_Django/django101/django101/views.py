from django.shortcuts import render


def index(req):
    context = {
        'name': 'Pako',
    }
    return render(req, 'index.html',context)

def opit(req):
    return render(req, 'opit.html')