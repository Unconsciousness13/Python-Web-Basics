from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def phones_list(request):
    return render(request, 'phones.html')
