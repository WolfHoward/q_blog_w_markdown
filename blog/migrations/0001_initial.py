# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
                'ordering': ['-created'],
            },
        ),
    ]
