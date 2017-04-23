# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 06:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contacto', models.CharField(max_length=50)),
                ('ape_contacto', models.CharField(max_length=50)),
                ('correo_contacto', models.EmailField(max_length=254)),
                ('fijo_contacto', models.IntegerField()),
                ('celu_contacto', models.IntegerField(null=True)),
                ('resum_problema', models.CharField(max_length=100)),
                ('detall_problema', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('asignado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Tecnico')),
                ('establecimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Establecimiento')),
                ('estado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Estado')),
                ('tema', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Tema')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
