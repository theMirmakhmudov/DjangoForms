from django.contrib import admin
from django.urls import path
from apps.views import forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', forms, name='forms')
]
