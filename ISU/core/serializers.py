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


class PassCard(serializers.ModelSerializer):
    class Meta:
        model = models.PassCard
        fields = '__all__'


class Subject(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'
