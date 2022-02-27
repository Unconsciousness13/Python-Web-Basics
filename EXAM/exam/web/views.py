from django.shortcuts import render, redirect

from exam.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from exam.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()

    album_count = len(albums)

    context = {
        'profile': profile,
        'album_count': album_count,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(context, pk):
    Album.objects.all().delete()
    Profile.objects.get(id=pk).delete()
    return redirect('/')


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def create_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
        'not_show_album': True,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    profile = get_profile()
    album = Album.objects.get(id=pk)
    context = {
        'album': album,
        'profile': profile
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'pk': pk,
        'not_show_album': False,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'pk': pk,
        'not_show_album': False,
    }
    return render(request, 'delete-album.html', context)
