# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_page_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(choices=[('HOME', 'Главная страница'), ('ABOUT', 'Страница об организации'), ('EDUCATION', 'Страница образование'), ('PAGE', 'Стандартная страница')], default='PAGE', max_length=500, verbose_name='Шаблон'),
        ),
    ]
