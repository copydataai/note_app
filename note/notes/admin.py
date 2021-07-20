"""Notes admin."""

# Django
from django.contrib import admin

# Utilities
from note.notes.models import Notes

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    """Notes admin."""
    list_display = (
        'slug_name',
        'title',
        'notes_made',
        'is_public',
        'is_edit'
    )
    search_fields = ('slug_name', 'title')
    list_filter = (
        'is_public',
        'is_edit'
    )
