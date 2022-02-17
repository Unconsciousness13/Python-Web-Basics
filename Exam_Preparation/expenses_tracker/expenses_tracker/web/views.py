from django.shortcuts import render, redirect


def get_profile():
    return 'ok'


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    return render(request, 'home-with-profile.html')


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request, pk):
    return render(request, 'expense-edit.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')


def show_profile(request):
    return render(request, 'profile.html')


def create_profile(request):
    return render(request, 'home-no-profile.html')


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')
