# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0007_auto_20151012_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_submission',
            name='running_time',
            field=models.CharField(max_length=100),
        ),
    ]
