from django.db import models
from apps.core.models import TimeStampedModel, Topic

# Create your models here.
class LearningResource(TimeStampedModel):
	"""
	A link to a learning resource associated with a specific Topic
	from a syllabus
	"""
	name = models.CharField(max_length=128, unique=False, null=True)
	link = models.URLField(default=None, blank=True, null=True)
	topic = models.ForeignKey('core.Topic', default=None, blank=True, null=True)
	summary = models.TextField(default=None, blank=True, null=True)