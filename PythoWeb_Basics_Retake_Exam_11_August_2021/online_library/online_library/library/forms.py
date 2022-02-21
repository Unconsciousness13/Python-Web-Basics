import os

from django import forms

from online_library.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Profile Image',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Profile Image',
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        self.instance.delete()
        Book.objects.all().delete()  # to delete all object conn to profile
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')


class DeleteBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.required = False

    # overriting save for delete
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'budget': 'Budget',
        #     'profile_image': 'Profile Image',
        # }