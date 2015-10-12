# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0002_auto_20151012_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='correct_answer',
            field=models.CharField(default=b'', max_length=10000),
        ),
    ]
