# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Updated',
            field=models.DateField(auto_now=True),
        ),
    ]
