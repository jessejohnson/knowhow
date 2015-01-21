from django.db import models
from django.template.defaultfilters import slugify
import uuid
from django.conf import settings

# Create your models here.
class TimeStampedModel(models.Model):
	"""
	abstract model with created_at and modified_at fields
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class BaseEntityModel(TimeStampedModel):
	"""
	abstract model for browseable entities with slugs
	"""
	name = models.CharField(max_length=128, unique=False, null=True)
	slug = models.SlugField(max_length=128, blank=True, null=True)

	def save(self, *args, **kwargs):
		#insert first seven characters of uuid before name for slug if no slug exists
		if self.id is None:
			self.slug = slugify(uuid.uuid1().hex[:7] + "-" + self.name)
		super(BaseEntityModel, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	class Meta:
		abstract = True

class Topic(BaseEntityModel):
	"""
	A unit of organisation that groups LearningContent into themes
	a student can request
	"""
	summary = models.TextField(default=None, blank=True, null=True)

class Exam(BaseEntityModel):
	"""
	An exam conducted by an examination body
	"""
	summary = models.TextField(default=None, blank=True, null=True)
	short_name = models.CharField(max_length=10, unique=False, null=True)

class Paper(BaseEntityModel):
	"""
	A paper belonging to an exam
	"""
	summary = models.TextField(default=None, blank=True, null=True)
	code = models.CharField(max_length=10, unique=False, null=True)