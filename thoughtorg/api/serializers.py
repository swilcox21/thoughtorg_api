from rest_framework import serializers

from .models import Thought

class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thought
        fields = ('content', 'folder')