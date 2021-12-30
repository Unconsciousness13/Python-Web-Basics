from django.contrib import admin
from django.urls import path

from second.phones.views import index, phones_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('phones/', phones_list)
]
