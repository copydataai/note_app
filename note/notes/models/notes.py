"""Notes model."""

# Django
from django.db import models

# Utilities
from note.utils.models import NoteModel

class Note(NoteModel):
    """Circle model.
    
    A Note is a private where 
    """

    title = models.CharField('note title', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)


    content = models.CharField('note description', max_length=300)
    picture = models.ImageField(upload_to='notes/pictures', blank=True, null=True)

    file = models.FileField(upload_to='notes/files/%Y/%m/%d/', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #Stats
    notes_made = models.PositiveIntegerField(default=0)

    is_public = models.BooleanField(
        default=True,
        help_text='The published notes are listed on the main page so that everyone knows about their existence'
    )

    is_edit = models.BooleanField(
        'editable',
        default=False,
        help_text='The note is not editable, except by the note user.'
    )

    def __str__(self):
        """Return note title."""
        return self.title

    class Meta(NoteModel.Meta):
        """Meta class."""
        ordering = ['-notes_made']
