from django import forms

from Recipes.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

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


class EditRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

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


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

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
