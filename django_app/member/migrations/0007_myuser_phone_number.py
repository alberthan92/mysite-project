# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20161023_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
