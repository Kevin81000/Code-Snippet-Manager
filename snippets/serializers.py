# project/snippets/serializers.py
from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'language', 'owner', 'created_at', 'public']