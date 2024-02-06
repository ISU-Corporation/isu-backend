from django.contrib import admin

from education import models


@admin.register(models.Schedule)
class Schedule(admin.ModelAdmin):
    pass


@admin.register(models.Subject)
class Subject(admin.ModelAdmin):
    pass

