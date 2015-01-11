from django.db import models
from django.template.defaultfilters import slugify
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

PAPERS = (
	('pap1', 'Paper 1'),
	)

EXAMS = (
	('ex1', 'exam1'),
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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)