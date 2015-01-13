# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, null=True)),
                ('slug', models.SlugField(max_length=128, null=True, blank=True)),
                ('exam', models.ForeignKey(default=None, blank=True, to='core.Exam', null=True)),
                ('paper', models.ForeignKey(default=None, blank=True, to='core.Paper', null=True)),
                ('topic', models.ForeignKey(default=None, blank=True, to='core.Topic', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, null=True)),
                ('slug', models.SlugField(max_length=128, null=True, blank=True)),
                ('question_number', models.PositiveIntegerField(default=None, null=True, blank=True)),
                ('question', models.ForeignKey(default=None, blank=True, to='questions.MultipleChoiceQuestion', null=True)),
                ('test', models.ForeignKey(default=None, blank=True, to='tests.Test', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
