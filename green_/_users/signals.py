from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserWallet


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff == False:
        UserWallet.objects.create(user=instance)
