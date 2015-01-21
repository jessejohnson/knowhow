# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='exam',
            field=models.ForeignKey(related_name='test_exam', default=None, blank=True, to='core.Exam', null=True),
            preserve_default=True,
        ),
    ]
