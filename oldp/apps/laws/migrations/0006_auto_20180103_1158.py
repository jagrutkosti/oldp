# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-03 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0005_auto_20180103_1151'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lawbook',
            unique_together=set([('code', 'revision_date')]),
        ),
    ]