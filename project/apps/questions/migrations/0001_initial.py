# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('case', models.TextField(default=None, null=True, blank=True)),
                ('exam', models.ForeignKey(default=None, blank=True, to='core.Exam', null=True)),
                ('paper', models.ForeignKey(default=None, blank=True, to='core.Paper', null=True)),
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
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(default=None, null=True, blank=True)),
                ('option_a', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_b', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_c', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_d', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('option_e', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('answer', models.CharField(default=None, max_length=3, null=True, blank=True, choices=[(b'A', b'Option A'), (b'B', b'Option B'), (b'C', b'Option C'), (b'D', b'Option D')])),
                ('exam', models.ForeignKey(default=None, blank=True, to='core.Exam', null=True)),
                ('paper', models.ForeignKey(default=None, blank=True, to='core.Paper', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='essayquestion',
            name='exam',
            field=models.ForeignKey(default=None, blank=True, to='core.Exam', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='essayquestion',
            name='paper',
            field=models.ForeignKey(default=None, blank=True, to='core.Paper', null=True),
            preserve_default=True,
        ),
    ]
