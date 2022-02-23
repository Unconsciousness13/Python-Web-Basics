from django.urls import path

from Notes.main.views import home_page, add_note, edit_note, delete_note, detail_note, profile_main, create_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', detail_note, name='details note'),
    path('create/', create_profile, name='profile create'),
    path('profile/', profile_main, name='profile main'),
)
