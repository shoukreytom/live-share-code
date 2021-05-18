# Generated by Django 3.2.3 on 2021-05-18 03:14

import codes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to=codes.models.upload_file_to)),
                ('collaborators', models.ManyToManyField(blank=True, related_name='collaborators', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codes.file')),
            ],
            options={
                'verbose_name_plural': 'Shared Files',
            },
        ),
    ]
