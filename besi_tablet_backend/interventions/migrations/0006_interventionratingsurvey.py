# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-12-10 02:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interventions', '0005_auto_20181210_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterventionRatingSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('Rating1', models.IntegerField(default=0)),
                ('value1', models.CharField(default='NA', max_length=300)),
                ('Rating2', models.IntegerField(default=0)),
                ('value2', models.CharField(default='NA', max_length=300)),
                ('Rating3', models.IntegerField(default=0)),
                ('value3', models.CharField(default='NA', max_length=300)),
                ('Rating4', models.IntegerField(default=0)),
                ('value4', models.CharField(default='NA', max_length=300)),
                ('deployment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]