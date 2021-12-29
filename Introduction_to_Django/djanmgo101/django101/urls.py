from django.contrib import admin
from django.urls import path

from django101.cities.views import index, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('test/', test),
]
