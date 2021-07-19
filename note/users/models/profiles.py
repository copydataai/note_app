"""Profile model."""

# Django
from django.db import models

# Utilities
from note.utils.models import NoteModel

class Profile(NoteModel):
    """Profile model.

    A profile holds a user's public data like biography, pictures
    and stats.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    notes_made = models.PositiveIntegerField(default=0)
    shared_notes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        """Return user's str representation."""
        return str(self.user)

