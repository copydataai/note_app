"""Notes serializers."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models 
from notes.note.models import Note

class NotesSerializer(serializers.Serializer):
    """Notes serializer."""
    title = serializers.CharField()
    slug_name = serializers.SlugField()
    modified = serializer.DateTimeField()
    

class CreateNotesSerializer(serializers.Serializer):
    """Create notes serializer."""
    
    title = serializers.CharField(max_length=140)
    
    slug_name = serializers.SlugField(
        max_length=40, 
        validators=[
            UniqueValidator(queryset=Note.objects.all())
        ]
    )
    content = serializers.CharField(max_length=300, required=False)
    picture = serializers.ImageField(required=False)
    file = serializers.FileField(required=False)

    def create(self, data):
        """Create Note"""
        return Note.objects.create(**data)


