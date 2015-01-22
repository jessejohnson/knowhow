from django.db import models
import uuid
from apps.core.models import TimeStampedModel

# Create your models here.
class Test(TimeStampedModel):
	"""
	A basic unit of assessment
	"""
	name = models.CharField(max_length=128, unique=False, null=True)
	exam = models.ForeignKey('core.Exam', default=None, blank=True, null=True, related_name='test_exam')
	paper = models.ForeignKey('core.Paper', default=None, blank=True, null=True)
	topic = models.ForeignKey('core.Topic', default=None, blank=True, null=True)

	# def save(self, *args, **kwargs):
	# 	#prefill name
	# 	if self.id is None:
	# 		self.name = self.exam.short_name + " " + self.paper.code + " " + self.topic.name
	# 	super(Test, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name + " " + self.id

class TestQuestionTable(TimeStampedModel):
	"""
	A table containing questions and their related tests in order
	"""
	name = models.CharField(max_length=128, unique=False, null=True)
	test = models.ForeignKey('Test', default=None, blank=True, null=True)
	question = models.ForeignKey('questions.MultipleChoiceQuestion', default=None, blank=True, null=True)
	question_number = models.PositiveIntegerField(default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		#prefill name
		self.name = self.test.name + " " + str(self.question_number)
		super(TestTable, self).save(*args, **kwargs)