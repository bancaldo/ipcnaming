# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-23 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(max_length=3)),
                ('prefix', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=256)),
                ('pattern', models.CharField(max_length=64)),
                ('arguments', models.CharField(max_length=256)),
            ],
        ),
    ]