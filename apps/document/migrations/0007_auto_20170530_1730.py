# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_auto_20170530_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alertmessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, null=True)),
                ('message', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
    ]
