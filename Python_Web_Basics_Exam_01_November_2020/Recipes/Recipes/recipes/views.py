from django.shortcuts import render, redirect

from Recipes.recipes.forms import CreateRecipeForm, DeleteRecipeForm
from Recipes.recipes.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_page(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm(instance=recipe)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'edit.html', context)


def delete_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'delete.html', context)


def delete_recipe(request, pk):
    Recipe.objects.get(id=pk).delete()
    return redirect('/')


def details_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'details.html', context)
