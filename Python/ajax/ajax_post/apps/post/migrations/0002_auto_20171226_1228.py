# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Note',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='post',
            new_name='note',
        ),
    ]
