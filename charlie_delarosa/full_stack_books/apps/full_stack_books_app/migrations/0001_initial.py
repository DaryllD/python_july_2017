# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=500)),
                ('publishedDate', models.IntegerField()),
                ('category', models.CharField(max_length=45)),
            ],
        ),
    ]
