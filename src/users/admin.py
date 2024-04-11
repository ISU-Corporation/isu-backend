from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users import models

admin.site.unregister(Group)


@admin.register(models.User)
class User(UserAdmin):
    list_display = ('username', 'is_superuser')
