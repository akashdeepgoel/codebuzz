# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Codemania', '0003_problem_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 14, 59, 6, 264533, tzinfo=utc), verbose_name=b'Addition Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem_submission',
            name='submitted_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 14, 59, 13, 767016, tzinfo=utc), verbose_name=b'Submission Time'),
            preserve_default=False,
        ),
    ]
