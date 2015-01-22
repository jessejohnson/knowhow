from django.contrib import admin
from .models import Test, TestQuestionTable

# Register your models here.
admin.site.register(Test)
admin.site.register(TestQuestionTable)