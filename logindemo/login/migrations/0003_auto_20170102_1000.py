# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170102_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authcode',
            name='create_time',
            field=models.CharField(max_length=30),
        ),
    ]