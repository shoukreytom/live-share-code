from django.db import models
from django.conf import settings


def upload_file_to(instance, filename):
    return f'files/{instance.owner.username}/{filename}'


class File(models.Model):
    slug = models.SlugField(max_length=250, blank=True)
    name = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to=upload_file_to)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='collaborators')

    def __str__(self):
        return self.name


class Shared(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE)
    code = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name_plural = 'Shared Files'
