from django.contrib import admin
from . import models


@admin.register(models.Customer)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscription', 'created', 'updated')
