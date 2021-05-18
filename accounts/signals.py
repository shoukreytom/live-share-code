from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account


@receiver(post_save, sender=Account)
def add_username_to_account(sender, instance, created, **kwargs):
    if created:
        instance.username = str(instance.email).split("@")[0]
        instance.save()
