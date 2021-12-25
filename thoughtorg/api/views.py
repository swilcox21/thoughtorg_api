from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ThoughtSerializer
from .models import Thought


class ThoughtViewSet(viewsets.ModelViewSet):
    queryset = Thought.objects.all().order_by('content')
    serializer_class = ThoughtSerializer
    