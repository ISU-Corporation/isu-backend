from rest_framework import serializers

from core import models


class Schedule(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'
