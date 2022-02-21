from django.urls import path

urlpatterns = (
    path('', show_index, name='show index'),

    path('add/', add_book, name='create book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='details page'),
    path('profile/', show_profile, name='show profile'),
    path('profile/', edit_profile, name='edit profile'),
    path('profile/', delete_profile, 'delete profile'),

)
