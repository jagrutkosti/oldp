# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-22 18:02
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0002_remove_law_foo'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedLaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=8, max_digits=12)),
                ('related_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_id', to='laws.Law')),
                ('seed_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seed_id', to='laws.Law')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]