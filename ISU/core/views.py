from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from core import models, serializers


class UserProfile(RetrieveAPIView, UpdateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfile


class Schedule(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.Schedule
