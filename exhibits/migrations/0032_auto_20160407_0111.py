# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0031_auto_20160406_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibititem',
            name='custom_crop',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/custom_item_crop/'),
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='custom_link',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='historicalessay',
            name='byline_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render byline as'),
        ),
        migrations.AlterField(
            model_name='historicalessay',
            name='color',
            field=models.CharField(blank=True, help_text='Please provide color in <code>#xxx</code>, <code>#xxxxxx</code>, <code>rgb(xxx,xxx,xxx)</code>, or <code>rgba(xxx,xxx,xxx,x.x)</code> formats.', max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalessay',
            name='go_further_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render as'),
        ),
    ]