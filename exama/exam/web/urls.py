from django.urls import path

from exam.web.views import show_index, create_album, album_details, album_edit, album_delete, profile_details, \
    delete_profile, create_profile

urlpatterns = (
    path('', show_index, name='show index'),

    path('album/add/', create_album, name='create album'),
    path('album/details/<int:pk>', album_details, name='album details'),
    path('album/edit/<int:pk>', album_edit, name='album edit'),
    path('profile/create/', create_profile, name='create profile'),
    path('album/delete/<int:pk>', album_delete, name='album delete'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
