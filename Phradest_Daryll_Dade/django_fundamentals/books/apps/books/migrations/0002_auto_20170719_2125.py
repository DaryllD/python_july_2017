# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='published_date',
            field=models.CharField(max_length=4),
        ),
    ]
