# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='todo.List'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=b''),
        ),
    ]
