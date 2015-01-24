from django.db import models
from apps.core.models import TimeStampedModel, Paper, Exam

OPTIONS = (
	('A', 'Option A'),
	('B', 'Option B'),
	('C', 'Option C'),
	('D', 'Option D'),
)

# Create your models here.
class BaseQuestion(TimeStampedModel):
	"""
	Base type for questions containing paper and exam fields
	"""
	paper = models.ForeignKey('core.Paper', default=None, blank=True, null=True)
	exam = models.ForeignKey('core.Exam', default=None, blank=True, null=True)

	def __unicode__(self):
		return "{} - {} - {}" .format(self.exam, self.paper, self.question)

	class Meta:
		abstract = True

class EssayQuestion(BaseQuestion):
	"""
	a question that demands a long written answer
	"""
	question = models.TextField(default=None, blank=True, null=True)

class MultipleChoiceQuestion(BaseQuestion):
	"""
	a question that demands answers from a selection of four possible answers
	"""
	question = models.TextField(default=None, blank=True, null=True)
	option_a = models.CharField(max_length=250, default=None, blank=True, null=True)
	option_b = models.CharField(max_length=250, default=None, blank=True, null=True)
	option_c = models.CharField(max_length=250, default=None, blank=True, null=True)
	option_d = models.CharField(max_length=250, default=None, blank=True, null=True)
	option_e = models.CharField(max_length=250, default=None, blank=True, null=True)
	answer = models.CharField(max_length=3, choices=OPTIONS, default=None, blank=True, null=True)

	def __unicode__(self):
		return "{} - {} - {}".format(self.exam.short_name, self.paper.name, self.question)
		
class CaseStudy(BaseQuestion):
	"""
	a case study that forms the preamble to CaseStudyQuestions
	"""
	case = models.TextField(default=None, blank=True, null=True)

class CaseStudyQuestion(EssayQuestion):
	"""
	an essay question that is preambled by a CaseStudy
	"""
	case_study = models.ForeignKey('CaseStudy', default=None, blank=True, null=True)