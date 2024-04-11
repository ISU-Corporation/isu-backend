from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat


class User(AbstractUser):
    patronymic = models.CharField('отчество', max_length=255, blank=True)
    full_name = models.GeneratedField(
        expression=Concat(
            models.F('last_name'),
            Value(' '),
            models.F('first_name'),
            Value(' '),
            models.F('patronymic')
        ),
        output_field=models.CharField('ФИО', max_length=255),
        db_persist=True,
    )
