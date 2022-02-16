from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.utils.html import format_html


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


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.profile_picture.url}" width="30" style="border-radius:50%;">')
    thumbnail.short_description = 'profile picture'
    list_display = ['thumbnail', 'user', 'city', 'state', 'country']
