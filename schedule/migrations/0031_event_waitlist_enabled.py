# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-03 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0030_inheritance'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='waitlist_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
