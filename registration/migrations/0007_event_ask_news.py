# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20160324_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ask_news',
            field=models.BooleanField(default=True, verbose_name='Ask if helper wants to be notified about new events'),
        ),
    ]
