# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studentrecords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='test',
            field=models.ForeignKey(default=None, blank=True, to='tests.Test', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentrecord',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
