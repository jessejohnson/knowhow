from django.contrib import admin
from .models import LearningContent, Topic

# Register your models here.
admin.site.register(LearningContent)
admin.site.register(Topic)