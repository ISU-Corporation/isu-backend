from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets

from core import models, serializers


class Schedule(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.Schedule
