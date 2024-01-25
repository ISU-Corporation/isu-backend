from django.contrib.auth.models import AbstractUser
from django.db import models

from core import consts


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    role = models.CharField(
        'роль',
        max_length=2,
        choices=consts.AUTH_STATUS_CHOICES,
        default=consts.AUTH_STATUS_STUDENT
    )
    first_name = models.CharField('имя', max_length=255)
    last_name = models.CharField('фамилия', max_length=255)
    patronymic = models.CharField('отчество', max_length=255)
    about_myself = models.TextField('о себе', blank=True)
    avatar = models.ImageField('аватар', upload_to='user_avatars/', null=True, blank=True)
    course_number = models.IntegerField('курс', null=True, blank=True)
    faculty = models.CharField('факультет', max_length=255)
    specialization = models.CharField('специальность', max_length=255)

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'

    @property
    def get_fullname(self) -> str:
        return ', '.join(filter(bool, (self.last_name, self.first_name, self.patronymic)))

    def __str__(self) -> str:
        return self.get_fullname


class Schedule(models.Model):
    subjects = models.ManyToManyField(
        'Subject',
        verbose_name='предметы',
        related_name='schedule',
    )
    date = models.DateField("дата", auto_now=True)

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'

    def __str__(self) -> models.DateField:
        return self.date


class PassCard(models.Model):
    mark = models.IntegerField('оценка', null=False, blank=True)
    student = models.ForeignKey(
        User,
        related_name='student',
        on_delete=models.CASCADE,
        verbose_name='ученик',
    )
    subject = models.ForeignKey(
        'Subject',
        related_name='pass_card',
        on_delete=models.DO_NOTHING,
        verbose_name="предмет",
    )

    class Meta:
        verbose_name = 'зачетная книжка'
        verbose_name_plural = 'зачетные книжки'


class Subject(models.Model):
    teacher = models.OneToOneField(
        User,
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
