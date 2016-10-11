# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=500)),
                ('extension', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='folder',
            name='Upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Upload'),
        ),
    ]