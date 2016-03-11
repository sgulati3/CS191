# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20160311_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='event',
            field=models.CharField(default='NA', max_length=2, choices=[('BR', 'Baltimore Uprising'), ('FP', 'Ferguson Protests'), ('SL', 'Stand With Leah'), ('NA', 'Not Currently Trending')]),
        ),
    ]
