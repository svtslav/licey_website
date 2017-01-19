# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=100, unique=True, verbose_name='URL'),
        ),
    ]
