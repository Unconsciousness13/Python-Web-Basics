
from django.contrib import admin
from django.urls import path

from django101.views import index,opit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('opit/', opit)
]
