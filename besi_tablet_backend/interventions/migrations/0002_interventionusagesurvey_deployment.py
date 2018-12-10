# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-12-09 23:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interventions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interventionusagesurvey',
            name='deployment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
