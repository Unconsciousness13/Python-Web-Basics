from django.shortcuts import render, redirect

from online_library.library.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateBookForm, \
    EditBookForm
from online_library.library.models import Book, Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    books = Book.objects.all()
    context = {
        'profile': profile,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def book_details(request):
    pass


def delete_book(request, pk):
    # expense = Expense.objects.get(pk=pk)
    # if request.method == 'POST':
    #     form = DeleteExpenseForm(request.POST, instance=expense)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show index')
    # else:
    #     form = DeleteExpenseForm(instance=expense)
    #
    # context = {
    #     'form': form,
    #     'expense': expense,
    # }
    #
    # return render(request, 'expense-delete.html', context)
    pass


def show_profile(request):
    profile = get_profile()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books,

    }
    return render(request, 'profile.html', context)


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


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


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
    return render(request, 'delete-profile.html', context)
