# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 06:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20160224_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='agitationsurvey',
            name='agitimestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 25, 6, 24, 11, 396435, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
