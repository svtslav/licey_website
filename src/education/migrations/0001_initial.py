# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ступень образования',
                'verbose_name_plural': 'Ступени образования',
            },
        ),
        migrations.CreateModel(
            name='EduPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='docs.DocumentCategory', verbose_name='Категория документов')),
            ],
            options={
                'verbose_name': 'Страница образование',
                'verbose_name_plural': 'Страницы образование',
            },
        ),
        migrations.CreateModel(
            name='EduProgram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link', models.URLField(blank=True, verbose_name='Страница образовательной программы')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.EduLevel', verbose_name='Ступень образования')),
            ],
            options={
                'verbose_name': 'Образовательная программа',
                'verbose_name_plural': 'Образовательные программы',
            },
        ),
        migrations.CreateModel(
            name='EduSection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
                ('show', models.BooleanField(default=False, verbose_name='Отображать на странице')),
            ],
            options={
                'verbose_name': 'Элемент страницы',
                'verbose_name_plural': 'Элементы страницы',
            },
        ),
    ]
