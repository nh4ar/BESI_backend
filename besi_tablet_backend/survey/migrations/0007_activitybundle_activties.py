# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20160316_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitybundle',
            name='activties',
            field=models.ManyToManyField(through='survey.ActivityBundleMember', to='survey.Activity'),
        ),
    ]
