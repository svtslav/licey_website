# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на документ')),
                ('file', models.FileField(blank=True, upload_to='docs/', verbose_name='Файл')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория документа',
                'verbose_name_plural': 'Категория документов',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docs.DocumentCategory'),
        ),
    ]
