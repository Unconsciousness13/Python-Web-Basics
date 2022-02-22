from django.shortcuts import render

from Recipes.recipes.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_page(request):
    pass


def edit_page(request):
    pass


def delete_page(request):
    pass


def details_page(request):
    pass
