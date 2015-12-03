# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', unique=True, max_length=100, verbose_name=b'slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True, max_length=100, verbose_name=b'slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 10, 29, 17, 33, 12, 850900, tzinfo=utc), unique=True, max_length=100, verbose_name=b'slug'),
            preserve_default=False,
        ),
    ]
