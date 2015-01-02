from django.contrib import admin
from .models import MultipleChoiceQuestion, EssayQuestion, CaseStudy, CaseStudyQuestion

# Register your models here.
admin.site.register(MultipleChoiceQuestion)
admin.site.register(EssayQuestion)
admin.site.register(CaseStudy)
admin.site.register(CaseStudyQuestion)