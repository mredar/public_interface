# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0002_auto_20160301_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalEssay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('blockquote', models.TextField(blank=True)),
                ('about_essay', models.TextField(blank=True)),
                ('essay', models.TextField(blank=True)),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='LessonPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('essay', models.TextField(blank=True)),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='NotesItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', positions.fields.PositionField(default=-1)),
                ('essay', models.TextField(blank=True)),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('color', models.CharField(blank=True, max_length=20)),
                ('about_theme', models.TextField(blank=True)),
                ('essay', models.TextField(blank=True)),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='exhibit',
            name='about_exhibit',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='blockquote',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='essay',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='essay',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='order',
            field=positions.fields.PositionField(default=-1),
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1),
        ),
        migrations.AddField(
            model_name='notesitem',
            name='exhibit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit'),
        ),
    ]
