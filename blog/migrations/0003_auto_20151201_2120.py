# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151029_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='the related category', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(max_length=1, default='D', choices=[('D', 'Not Reviewed'), ('P', 'Published'), ('E', 'Expired')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(verbose_name='the related tags', blank=True, to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='views_count',
            field=models.IntegerField(verbose_name='views count', default=0),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug', max_length=100),
        ),
    ]
