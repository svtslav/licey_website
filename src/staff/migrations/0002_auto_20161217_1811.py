# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='education',
            field=models.CharField(blank=True, max_length=500, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='person',
            name='teaching_experience',
            field=models.CharField(blank=True, max_length=200, verbose_name='Педагогический стаж'),
        ),
    ]
