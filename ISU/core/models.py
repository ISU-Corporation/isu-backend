from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    class Status:
        pass


class Subject(models.Model):
    pass


class Schedule(models.Model):
    pass


class PassCard(models.Model):
    pass
