# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170719_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='in_print',
            field=models.BooleanField(default=True),
        ),
    ]
