from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from core import models, serializers


class UserProfile(RetrieveAPIView, UpdateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfile


class Schedule(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.Schedule


class PassCard(viewsets.ModelViewSet):
    queryset = models.PassCard.objects.all()
    serializer_class = serializers.PassCard


class Subject(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.Subject
