# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-09 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0008_auto_20180209_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='name',
            field=models.CharField(help_text='Full name of the court with location', max_length=200),
        ),
        migrations.AlterField(
            model_name='court',
            name='wikipedia_title',
            field=models.CharField(blank=True, help_text='Title of the corresponding Wikipedia article', max_length=200, null=True),
        ),
    ]