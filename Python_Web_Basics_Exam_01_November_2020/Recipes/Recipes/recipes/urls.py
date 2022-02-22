from django.urls import path

from Recipes.recipes.views import home_page, create_page, edit_page, delete_page, details_page

urlpatterns = (
    path('', home_page, name='home page'),
    path('create', create_page, name='create page'),
    path('edit/<int:pk>', edit_page, name='edit page'),
    path('delete/<int:pk>', delete_page, name='delete page'),
    path('details/<int:pk>', details_page, name='details page'),

)
