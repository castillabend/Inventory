# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20180817_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departure',
            name='id_inventory',
        ),
        migrations.AlterField(
            model_name='departure',
            name='id_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Brand'),
        ),
    ]
