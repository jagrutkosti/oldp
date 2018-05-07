# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-09 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0006_auto_20180130_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='wikipedia_title',
            field=models.CharField(help_text='Title of the corresponding Wikipedia article', max_length=100, null=True),
        ),
    ]