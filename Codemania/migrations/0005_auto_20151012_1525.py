# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0004_auto_20151012_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='problem',
            new_name='problem_statement',
        ),
    ]
