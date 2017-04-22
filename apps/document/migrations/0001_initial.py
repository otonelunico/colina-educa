# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('mat', models.CharField(max_length=50)),
                ('cuerpo', models.TextField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('desde', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='document.Desde')),
            ],
        ),
        migrations.CreateModel(
            name='Para',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_docum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='documento',
            name='para',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='document.Para'),
        ),
        migrations.AddField(
            model_name='documento',
            name='tipo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='document.Tipo_docum'),
        ),
    ]
