# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20160316_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Genre'),
        ),
    ]
