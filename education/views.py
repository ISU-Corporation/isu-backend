from rest_framework import viewsets

from education import models, serializers


class Schedule(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.Schedule


class Subject(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.Subject


class Homework(viewsets.ModelViewSet):
    queryset = models.Homework.objects.all()
    serializer_class = serializers.Homework
