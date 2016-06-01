# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-09 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0037_auto_20160505_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notesitem',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='browsetermgroup',
            name='exhibit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit'),
        ),
        migrations.AddField(
            model_name='browsetermgroup',
            name='exhibit_order',
            field=positions.fields.PositionField(default=-1),
        ),
        migrations.AlterField(
            model_name='browsetermgroup',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exhibits.Theme'),
        ),
    ]
