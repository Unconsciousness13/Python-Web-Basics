from django.shortcuts import render


def index(req):
    return render(req, 'index.html')

def test(req):
    return render(req, 'test.html')