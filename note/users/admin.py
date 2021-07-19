"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# models
from note.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'notes_made', 'shared_notes')
    search_field = ('user__username', 'user__email', 'user__first_name', 'user__last_name')


admin.site.register(User, CustomUserAdmin)
