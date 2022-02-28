import os

from django import forms

from exam.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }

        widgets = {
            "username": forms.TextInput(attrs={
                "type": "text", "name": "username", "id": "first_name",
                "placeholder": "Username"
            }),
            "email": forms.EmailInput(attrs={
                "type": "text", "name": "email", "id": "email",
                "placeholder": "Email"
            }),

            "age": forms.NumberInput(attrs={
                "type": "number", "name": "age", "id": "age",
                "placeholder": "Age", "min": "0"
            })
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()  # to delete all object conn to profile
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'img_url', 'price')

        widgets = {
            "album_name": forms.TextInput(attrs={
                "type": "text", "name": "name", "required": True,
                "placeholder": "Album Name"
            }),
            "artist": forms.TextInput(attrs={
                "type": "text", "id": "artist",
                "placeholder": "Artist", "required": True
            }),

            "description": forms.Textarea(attrs={
                "name": "genre", "id": "description", "placeholder": "Description", "Description": "Album Name"
            }),
            "img_url": forms.URLInput(attrs={
                "type": "url", "placeholder": "Image URL", "required": True, "id": "imgUrl"
            }),
            "price": forms.NumberInput(attrs={
                "id": "price", "type": "number", "placeholder": "price", "required": True, "min": "0"
            })
        }
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'img_url': 'Image URL',
            'price': 'Price',

        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'img_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'img_url': 'Image URL',
            'price': 'Price',

        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'img_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'img_url': 'Image URL',
            'price': 'Price',

        }
