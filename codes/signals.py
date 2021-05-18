from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from datetime import datetime

from .models import File


@receiver(post_save, sender=File)
def add_name_and_slug(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.name:
            instance.name = f"untitled-"+slugify(str(datetime.now()))
            instance.slug = slugify(instance.name)
        else:
            instance.slug = slugify(instance.name+slugify(str(datetime.now())))
        instance.save()
