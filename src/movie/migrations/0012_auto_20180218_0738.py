# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import movie.validators


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20180217_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Studio',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[movie.validators.validacion_studio, movie.validators.validacion_studio1]),
        ),
    ]
