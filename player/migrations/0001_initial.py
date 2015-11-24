# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(verbose_name='date of creation', default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(verbose_name='date of update', default=django.utils.timezone.now)),
                ('registration_ip', models.CharField(default='', max_length=15)),
                ('user', models.OneToOneField(null=True, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'player profile',
                'verbose_name_plural': 'players profiles',
            },
        ),
    ]
