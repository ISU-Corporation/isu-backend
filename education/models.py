from django.db import models


class Subject(models.Model):
    teacher = models.OneToOneField(
        'core.User',
        related_name='subject',
        on_delete=models.DO_NOTHING,
        verbose_name='преподаватель',
    )
    subject = models.CharField('предмет', max_length=255, blank=False)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self) -> str:
        return str(self.subject)


class Homework(models.Model):
    subject = models.OneToOneField(
        Subject,
        related_name='homework',
        on_delete=models.CASCADE,
        verbose_name='предмет',
    )
    task = models.TextField(
        'задание',
        blank=False,
    )
    mark = models.IntegerField(
        'оценка',
        null=False,
        blank=True,
    )

    class Meta:
        verbose_name = 'домашнее задание'

    def __str__(self) -> str:
        return self.task


class Schedule(models.Model):
    subjects = models.ManyToManyField(
        Subject,
        verbose_name='предметы',
        related_name='schedule',
    )
    date = models.DateField(
        "дата",
        auto_now=True
    )

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'

    def __str__(self) -> models.DateField:
        return self.date
