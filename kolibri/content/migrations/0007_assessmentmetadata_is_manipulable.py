# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20170307_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentmetadata',
            name='is_manipulable',
            field=models.BooleanField(default=False),
        ),
    ]