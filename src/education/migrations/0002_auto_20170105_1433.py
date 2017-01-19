# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='EduCourseAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.EduCourse', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Аннотация дисциплины',
                'verbose_name_plural': 'Аннотации дисциплин',
            },
        ),
        migrations.RemoveField(
            model_name='edupage',
            name='documents',
        ),
        migrations.DeleteModel(
            name='EduSection',
        ),
        migrations.AlterField(
            model_name='edulevel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='EduPage',
        ),
        migrations.AddField(
            model_name='educourse',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.EduProgram', verbose_name='Образовательная программа'),
        ),
    ]
