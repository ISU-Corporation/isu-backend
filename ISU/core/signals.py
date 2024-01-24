from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import User, UserProfile


@receiver(post_save, sender=User)
def create_profile(sender: User, instance: User, created: bool, **kwargs: dict) -> None:
    if created:
        UserProfile.objects.create(user=instance)
