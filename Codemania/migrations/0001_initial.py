# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem_submissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submission', models.CharField(max_length=4000000)),
                ('status', models.CharField(max_length=20)),
                ('running_time', models.IntegerField()),
                ('submitted_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem', models.CharField(max_length=5000)),
                ('title', models.CharField(max_length=10)),
                ('problem_name', models.CharField(max_length=200)),
                ('test_cases', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='problem_submissions',
            name='problem_title',
            field=models.ForeignKey(to='Codemania.Problems'),
        ),
    ]
