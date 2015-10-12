# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0008_auto_20151012_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_submission',
            name='problem_title',
            field=models.CharField(max_length=100),
        ),
    ]
