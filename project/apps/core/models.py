from django.db import models
from django.template.defaultfilters import slugify
import uuid
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class TimeStampedModel(models.Model):
	"""
	abstract model with created_at and modified_at fields
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Topic(TimeStampedModel):
	"""
	A unit of organisation that groups LearningContent into themes
	a student can request
	"""
	name = models.CharField(max_length=128, unique=False, null=True)

	def __unicode__(self):
		return self.name

class Exam(TimeStampedModel):
	"""
	An exam conducted by an examination body
	"""
	name = models.CharField(max_length=128, unique=False, null=True)
	short_name = models.CharField(max_length=10, unique=False, null=True)

	def __unicode__(self):
		return "{} - {}".format(self.short_name, self.name)

class Paper(TimeStampedModel):
	"""
	A paper belonging to an exam
	"""
	name = models.CharField(max_length=128, unique=False, null=True)
	code = models.CharField(max_length=20, unique=False, null=True)

	def __unicode__(self):
		return "{} - {}".format(self.code, self.name)

class UserManager(BaseUserManager):

	def create_user(self, username, email, password=None):
		"""
		Create user with given username, email and password
		"""
		if not email:
			raise ValueError('User must have an email address')
		user = self.model(username=username, email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		"""
		Create superuser with given username, email and password
		"""
		user = self.create_user(username=username, email=email, password=password)
		user.is_admin = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):

	username = models.CharField(verbose_name='username', max_length=255, unique=True, blank=False, null=True)
	email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=False, null=True)
	first_name = models.CharField(max_length=255, unique=False, blank=True, null=True)
	last_name = models.CharField(max_length=255, unique=False, blank=True, null=True)
	avatar = models.FileField(upload_to='media_uploads', default=None, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


	def get_full_name(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def get_short_name(self):
		return self.username

	def __unicode__(self):
		return self.username + " " + self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to the app app_label?"
		return True

	@property
	def is_staff(self):
		return self.is_admin

# post save user to add auth token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)







# class BaseEntityModel(TimeStampedModel):
# 	"""
# 	abstract model for browseable entities with slugs
# 	"""
# 	name = models.CharField(max_length=128, unique=False, null=True)
# 	slug = models.SlugField(max_length=128, blank=True, null=True)

# 	def save(self, *args, **kwargs):
# 		#insert first seven characters of uuid before name for slug if no slug exists
# 		if self.id is None:
# 			self.slug = slugify(uuid.uuid1().hex[:7] + "-" + self.name)
# 		super(BaseEntityModel, self).save(*args, **kwargs)

# 	def __unicode__(self):
# 		return self.name

# 	class Meta:
# 		abstract = True