# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 17:07
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
        ('laws', '0002_remove_law_foo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.TextField()),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Case')),
                ('law', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.Law')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseReferenceMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('uuid', models.CharField(max_length=36)),
                ('start', models.IntegerField(default=0)),
                ('end', models.IntegerField(default=0)),
                ('line', models.CharField(blank=True, max_length=200)),
                ('referenced_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.Case')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LawReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.TextField()),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Case')),
                ('law', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='laws.Law')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LawReferenceMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('uuid', models.CharField(max_length=36)),
                ('start', models.IntegerField(default=0)),
                ('end', models.IntegerField(default=0)),
                ('line', models.CharField(blank=True, max_length=200)),
                ('referenced_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laws.Law')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lawreference',
            name='marker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.LawReferenceMarker'),
        ),
        migrations.AddField(
            model_name='casereference',
            name='marker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.CaseReferenceMarker'),
        ),
    ]