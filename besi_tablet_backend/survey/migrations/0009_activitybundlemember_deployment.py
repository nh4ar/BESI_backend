# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 00:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0008_auto_20160317_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitybundlemember',
            name='deployment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
