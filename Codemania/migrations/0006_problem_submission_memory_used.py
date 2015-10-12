# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0005_auto_20151012_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem_submission',
            name='memory_used',
            field=models.CharField(default=3464, max_length=100),
            preserve_default=False,
        ),
    ]
