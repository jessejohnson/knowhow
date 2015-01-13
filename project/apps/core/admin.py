from django.contrib import admin
from .models import Topic, Exam, Paper

# Register your models here.
admin.site.register(Topic)
admin.site.register(Exam)
admin.site.register(Paper)