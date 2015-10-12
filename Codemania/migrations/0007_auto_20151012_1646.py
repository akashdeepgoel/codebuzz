# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0006_problem_submission_memory_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_submission',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
