from django import forms

from Recipes.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time',)
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)'
        }
