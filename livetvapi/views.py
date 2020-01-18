from django.shortcuts import render
from rest_framework import viewsets
from livetvapi import serializers
from livetvapi import models
# Create your views here.

class LiveTvViewSet(viewsets.ModelViewSet):
    """Handle createing, reading and updating LiveTv API Data"""
    serializer_class = serializers.TvLinkSerializer
    queryset = models.TvLink.objects.all()