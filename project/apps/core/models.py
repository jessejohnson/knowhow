from django.db import models
from django.template.defaultfilters import slugify
import uuid

PAPERS = (
	('0351/1', 'Human Resource Management Paper I'),
	('0351/2', 'Human Resource Management Paper II'),
	('P1011', 'Business Management Paper I'),
	('P1012', 'Business Management Paper II'),
)

EXAMS = (
	('WASSCE', 'West African Senior School Certificate Examination'),
	('ABCE', 'Advanced Business Certificate Examination'),
)

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