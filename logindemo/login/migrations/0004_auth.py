# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170102_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.CharField(max_length=30)),
                ('random_code', models.CharField(max_length=30)),
            ],
        ),
    ]
