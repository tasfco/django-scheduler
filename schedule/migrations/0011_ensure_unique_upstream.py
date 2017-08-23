# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_event_asana_id'),
    ]

    operations = [
        migrations.RunSQL('''
DO $$
BEGIN

  BEGIN
    ALTER TABLE schedule_event ADD CONSTRAINT schedule_event_unique_upstream UNIQUE (upstream_id, upstream_type);
    EXCEPTION
    WHEN DUPLICATE_TABLE THEN RAISE NOTICE 'Table constraint schedule_event_unique_upstream already exists';
  END;

END $$;
        ''')
    ]
