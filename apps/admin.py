from django.contrib import admin
from apps.models import Contact


@admin.register(Contact)
class Admin(admin.ModelAdmin):
    pass