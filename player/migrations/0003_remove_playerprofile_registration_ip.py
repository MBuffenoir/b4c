# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20151124_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerprofile',
            name='registration_ip',
        ),
    ]
