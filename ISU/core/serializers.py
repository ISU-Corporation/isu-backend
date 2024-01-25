from rest_framework import serializers

from core import models


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'


class Schedule(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'
