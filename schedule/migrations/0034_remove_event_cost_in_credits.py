# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-29 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0033_templates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='cost_in_credits',
        ),
    ]
