# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('core', '0002_auto_20161215_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='staff.Person', verbose_name='Директор'),
        ),
    ]