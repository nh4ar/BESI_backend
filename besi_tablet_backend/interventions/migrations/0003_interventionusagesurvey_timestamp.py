# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-12-09 23:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interventions', '0002_interventionusagesurvey_deployment'),
    ]

    operations = [
        migrations.AddField(
            model_name='interventionusagesurvey',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 23, 54, 44, 852386, tzinfo=utc)),
            preserve_default=False,
        ),
    ]