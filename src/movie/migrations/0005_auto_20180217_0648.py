# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Gender',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('publich', 'publich'), ('private', 'Private')], default='draft', max_length=120),
        ),
    ]