# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-19 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0011_auto_20161219_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='file_url',
            field=models.CharField(default='sdfdsf', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachment',
            name='size',
            field=models.CharField(default='dsfds', max_length=32),
            preserve_default=False,
        ),
    ]