# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_activitybundle_activties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitybundle',
            old_name='activties',
            new_name='activities',
        ),
    ]
