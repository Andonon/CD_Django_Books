# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksmodel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bikes',
            new_name='Books',
        ),
    ]