# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 01:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20170605_1253'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarItem',
            new_name='CartItem',
        ),
    ]
