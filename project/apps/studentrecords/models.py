from django.db import models
from django.conf import settings
from apps.core.models import BaseEntityModel

# Create your models here.
class StudentRecord(BaseEntityModel):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	test = models.ForeignKey('tests.Test', default=None, blank=True, null=True)
	grade = models.PositiveIntegerField(default=None, blank=True, null=True)

	def save(self, *args, **kwargs):
		#prefill name
		self.name = self.user.username + " " + self.test.name
		super(StudentRecord, self).save(*args, **kwargs)