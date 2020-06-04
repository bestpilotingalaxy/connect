from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Receive a signal when user signed up.
    Create a profile model with additional fields based on user data.
    """
    if created:
        UserProfile.objects.create(user=instance)
