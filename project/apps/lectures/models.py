from django.db import models
from apps.core.models import BaseEntityModel, Topic

# Create your models here.
class LearningResource(BaseEntityModel):
	"""
	A link to a learning resource associated with a specific Topic
	from a syllabus
	"""
	link = models.URLField(default=None, blank=True, null=True)
	topic = models.ForeignKey('core.Topic', default=None, blank=True, null=True)
	summary = models.TextField(default=None, blank=True, null=True)