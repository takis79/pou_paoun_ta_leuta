# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisations', '0005_auto_20160725_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='office',
            name='revised',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='suboffice',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='suboffice',
            name='revised',
            field=models.BooleanField(default=False),
        ),
    ]
