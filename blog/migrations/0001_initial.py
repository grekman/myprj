# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('status', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Not Reviewed'), (b'P', b'Published'), (b'E', b'Expired')])),
                ('enable_comment', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('created_date', models.DateTimeField()),
                ('views_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'name')),
                ('description', models.TextField(max_length=4096)),
                ('views_count', models.IntegerField(default=0, verbose_name=b'views count')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'the related category', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'the related tags', blank=True),
        ),
    ]
