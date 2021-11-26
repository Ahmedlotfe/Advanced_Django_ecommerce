from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.Account)
class AccountAdmin(UserAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'username', 'last_login', 'date_joined', 'is_active']
    list_display_links = ['email', 'first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']
    ordering = ['-date_joined']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
