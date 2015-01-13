from django.db import models
import uuid
from apps.core.models import BaseEntityModel, TimeStampedModel

# Create your models here.
class Test(BaseEntityModel):
	exam = models.ForeignKey('core.Exam', default=None, blank=True, null=True)
	paper = models.ForeignKey('core.Paper', default=None, blank=True, null=True)
	topic = models.ForeignKey('core.Topic', default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		#prefill name
		if self.id is None:
			self.name = self.exam.short_name + " " + self.paper.code + " " + self.topic.name + " " + uuid.uuid1().hex[:7]
		super(Test, self).save(*args, **kwargs)

class TestTable(BaseEntityModel):
	test = models.ForeignKey('Test', default=None, blank=True, null=True)
	question = models.ForeignKey('questions.MultipleChoiceQuestion', default=None, blank=True, null=True)
	question_number = models.PositiveIntegerField(default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		#prefill name
		self.name = self.test.name + " " + str(self.question_number)
		super(TestTable, self).save(*args, **kwargs)