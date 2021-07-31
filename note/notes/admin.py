"""Notes admin."""

# Django
from django.contrib import admin

# Utilities
from note.notes.models import Note

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    """Notes admin."""
    list_display = (
        'slug_name',
        'title',
        'notes_made',
        'is_public',
    )
    search_fields = ('slug_name', 'title')
    list_filter = (
        'is_public',
    )
