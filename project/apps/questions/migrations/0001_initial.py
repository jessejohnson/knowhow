# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('paper', models.CharField(default=None, max_length=128, null=True, blank=True, choices=[(b'0351/1', b'Human Resource Management Paper I'), (b'0351/2', b'Human Resource Management Paper II'), (b'P1011', b'Business Management Paper I'), (b'P1012', b'Business Management Paper II')])),
                ('exam', models.CharField(default=None, max_length=128, null=True, blank=True, choices=[(b'WASSCE', b'West African Senior School Certificate Examination'), (b'ABCE', b'Advanced Business Certificate Examination')])),
                ('case', models.TextField(default=None, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EssayQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('paper', models.CharField(default=None, max_length=128, null=True, blank=True, choices=[(b'0351/1', b'Human Resource Management Paper I'), (b'0351/2', b'Human Resource Management Paper II'), (b'P1011', b'Business Management Paper I'), (b'P1012', b'Business Management Paper II')])),
                ('exam', models.CharField(default=None, max_length=128, null=True, blank=True, choices=[(b'WASSCE', b'West African Senior School Certificate Examination'), (b'ABCE', b'Advanced Business Certificate Examination')])),
                ('question', models.TextField(default=None, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaseStudyQuestion',
            fields=[
                ('essayquestion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='questions.EssayQuestion')),
                ('case_study', models.ForeignKey(default=None, blank=True, to='questions.CaseStudy', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('questions.essayquestion',),
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('paper', models.CharField(default=None, max_length=128, null=True, blank=True, choices=[(b'0351/1', b'Human Resource Management Paper I'), (b'0351/2', b'Human Resource Management Paper II'), (b'P1011', b'Business Management Paper I'), (b'P1012', b'Business Management Paper II')])),
                ('exam', models.CharField(default=None, max_length=128, null=True, blank=True, choices=[(b'WASSCE', b'West African Senior School Certificate Examination'), (b'ABCE', b'Advanced Business Certificate Examination')])),
                ('question', models.TextField(default=None, null=True, blank=True)),
                ('option_a', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_b', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_c', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_d', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('answer', models.CharField(default=None, max_length=3, null=True, blank=True, choices=[(b'A', b'Option A'), (b'B', b'Option B'), (b'C', b'Option C'), (b'D', b'Option D')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
