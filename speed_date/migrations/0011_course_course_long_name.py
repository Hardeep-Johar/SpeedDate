# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed_date', '0010_course_rotation_freeze'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_long_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
