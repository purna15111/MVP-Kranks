# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-19 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_in',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('pass_word', models.CharField(max_length=25)),
            ],
        ),
    ]