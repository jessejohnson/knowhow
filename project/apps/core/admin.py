from django.contrib import admin
from .models import Topic, Exam, Paper, User
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Topic)
admin.site.register(Exam)
admin.site.register(Paper)
admin.site.register(User)

admin.site.unregister(Group)