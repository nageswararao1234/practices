# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-03 16:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='start_at',
        ),
    ]