# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0009_auto_20151012_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='solvedby',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
