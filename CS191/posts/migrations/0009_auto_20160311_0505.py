# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20160311_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]