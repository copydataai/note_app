"""Notes views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Permissions
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Serializers
from note.notes.serializers import NoteModelSerializer

# Models
from note.notes.models import Note


class NoteViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """Note view set."""
    serializer_class = NoteModelSerializer
    lookup_field = 'slug_name'

    # Filters
