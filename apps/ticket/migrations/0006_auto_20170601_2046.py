# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20170601_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='ticket',
            field=models.IntegerField(null=True),
        ),
    ]
