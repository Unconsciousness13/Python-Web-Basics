from django.shortcuts import render, redirect

from Notes.main.forms import CreateProfileForm, CreateNoteForm, EditNoteForm
from Notes.main.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')

    notes = Note.objects.all()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
        'not_show_note': True,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'pk': pk,
        'not_show_note': False,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    Note.objects.get(id=pk).delete()
    return redirect('/')


def detail_note(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def profile_main(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request, pk):
    Note.objects.all().delete()
    Profile.objects.get(id=pk).delete()
    return redirect('/')
