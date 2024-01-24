from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    class Status:
        pass


class Schedule(models.Model):
    data = models.DateField("день", null=True)


class PassCard(models.Model):
    mark = models.IntegerField('оценка', null=False)
    student = models.OneToOneField(User, verbose_name='ученик', related_name='passcard', on_delete=models.CASCADE,
                                   primary_key=True)


class Subject(models.Model):
    schedule = models.ManyToManyField(Schedule, verbose_name='расписание', related_name='subject')
    passcard = models.ForeignKey(PassCard, verbose_name="зачетная книжка", related_name="subject",
                                 on_delete=models.DO_NOTHING)
    teacher = models.OneToOneField(User, verbose_name='преподаватель', related_name='subject',
                                   on_delete=models.DO_NOTHING, primary_key=True)
    name = models.CharField('названиe', max_length=50, blank=False)

    def __str__(self):
        return str(self.name)
