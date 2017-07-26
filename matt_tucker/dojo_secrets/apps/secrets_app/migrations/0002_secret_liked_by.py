# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_user_friends'),
        ('secrets_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='login_app.User'),
        ),
    ]
