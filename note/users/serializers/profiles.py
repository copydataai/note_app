"""Profile model."""

# Django REST Framework
from rest_framework import serializers

# Models
from note.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'biography',
            'notes_made',
            'shared_notes'
        )
        read_only_fields = (
            'notes_made',
            'shared_notes'
        )
