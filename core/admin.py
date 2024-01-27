from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core import models


@admin.register(models.User)
class User(UserAdmin):
    pass


@admin.register(models.UserProfile)
class UserProfile(admin.ModelAdmin):
    pass


@admin.register(models.Schedule)
class Schedule(admin.ModelAdmin):
    pass


@admin.register(models.PassCard)
class PassCard(admin.ModelAdmin):
    pass


@admin.register(models.Subject)
class Subject(admin.ModelAdmin):
    pass
