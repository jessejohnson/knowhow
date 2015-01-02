from django.db import models
from apps.core.models import BaseEntityModel

# Create your models here.
class LearningContent(BaseEntityModel):
	"""
	A link to a learning resource associated with a specific Topic
	from a syllabus
	"""
	link = models.URLField(default=None, blank=True, null=True)
	topic = models.ForeignKey('Topic', default=None, blank=True, null=True)
	summary = models.TextField(default=None, blank=True, null=True)

class Topic(BaseEntityModel):
	"""
	A unit of organisation that groups LearningContent into themes
	a student can request
	"""
	summary = models.TextField(default=None, blank=True, null=True)