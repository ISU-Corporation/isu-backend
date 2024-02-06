from rest_framework import serializers

from education import models


class Schedule(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'


class Subject(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'


class Homework(serializers.ModelSerializer):
    class Meta:
        model = models.Homework
        fields = '__all__'
