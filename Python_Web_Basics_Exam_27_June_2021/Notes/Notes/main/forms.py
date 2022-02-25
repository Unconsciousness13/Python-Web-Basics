from django import forms
from django.shortcuts import render

from Notes.main.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class CreateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to image',
        }


class EditNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to image',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)


class NoteDetails(forms.ModelForm):
    def get_note(self, request, pk):
        note = Note.objects.get(id=pk)
        return render(request, "note-details.html", {"note": note})
